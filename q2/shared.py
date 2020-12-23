import re
import os


def unpack_policy(line):
    res = re.findall(r'(\d+)-(\d+) (\w): (\w+)', line)[0]
    min_val, max_val, policy_char, password = res
    return int(min_val), int(max_val), policy_char, password


def read_db():
    txt_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(txt_file) as f:
        for line in f:
            yield line
