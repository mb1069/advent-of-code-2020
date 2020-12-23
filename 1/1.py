from shared import read_txt_single_col_nums
from itertools import permutations
import os


def main():
    txt_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    numbers = read_txt_single_col_nums(txt_file, int)
    for n1, n2 in permutations(numbers, 2):
        if n1 + n2 == 2020:
            print(n1 * n2)
            break


if __name__ == '__main__':
    main()
