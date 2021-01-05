import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        txt = f.read()
    txt = txt.strip()
    return list(map(int, txt.split(',')))
