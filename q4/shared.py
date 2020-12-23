import os
import re


def process_raw_passport(txt):
    txt = txt.replace('\n', ' ')
    field_values = re.findall(r'(\w+):([^\s]+)\s?', txt)
    return dict(field_values)


def read_passport_data():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        txt = f.read()

    passports = [process_raw_passport(p) for p in txt.split('\n\n')]

    return passports
