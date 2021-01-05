import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        lines = f.readlines()
    return [r.strip() for r in lines]
