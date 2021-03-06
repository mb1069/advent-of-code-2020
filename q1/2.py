import os
from functools import reduce

from q1.shared import read_txt_single_col_nums, get_permutations_with_sum


def main():
    txt_file = os.path.join(os.path.dirname(__file__), os.pardir, 'q1', 'input.txt')
    numbers = read_txt_single_col_nums(txt_file, int)
    summing_numbers = get_permutations_with_sum(numbers, 3, 2020)
    print(reduce(lambda a, b: a * b, summing_numbers))


if __name__ == '__main__':
    main()
