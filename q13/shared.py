import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        txt = f.readlines()
    earliest_timestamp = int(txt[0].strip())
    buses = txt[1].strip().split(',')
    return earliest_timestamp, buses
