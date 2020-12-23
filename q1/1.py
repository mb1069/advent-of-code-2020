import os

from q1.shared import read_txt_single_col_nums, get_permutations_with_sum


def main():
    txt_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    numbers = read_txt_single_col_nums(txt_file, int)
    n1, n2 = get_permutations_with_sum(numbers, 2, 2020)
    print(n1 * n2)


if __name__ == '__main__':
    main()
