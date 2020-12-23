from itertools import permutations
from typing import Union


def read_txt_single_col_nums(txtfile: str, dtype: Union[int, float]):
    with open(txtfile) as f:
        raw_lines = f.readlines()
    numbers = [dtype(l.strip()) for l in raw_lines]

    return numbers


def get_permutations_with_sum(numbers, k, total):
    for numbs in permutations(numbers, k):
        if sum(numbs) == total:
            return numbs
    raise ValueError('No combination of numbers found')
