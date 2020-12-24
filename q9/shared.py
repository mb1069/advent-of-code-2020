import os
from itertools import combinations


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        yield from f


def calc_sums(previous_numbers):
    return {a + b for a, b in combinations(previous_numbers, 2)}


def find_preamble_limit(preamble_length):
    preamble_sums = set()
    preamble_numbers = []
    for i, l in enumerate(read_file()):
        l = int(l.strip())

        # Construct initial set of sums
        if len(preamble_numbers) == preamble_length:
            preamble_sums = calc_sums(preamble_numbers)

        if l not in preamble_sums and i > preamble_length:
            return l

        if len(preamble_numbers) == preamble_length:
            preamble_numbers.pop(0)
        preamble_numbers.append(l)

        print(l, preamble_numbers, preamble_sums)