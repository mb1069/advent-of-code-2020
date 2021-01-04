import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        txt = f.readlines()
    return [t.strip() for t in txt]