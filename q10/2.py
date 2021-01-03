from q10.shared import read_file
import numpy as np


def create_adjacency_matrix(nums):
    n = len(nums)
    m = np.zeros((n, n))
    for i, n in enumerate(nums):
        for _i2, n2 in enumerate(nums[i + 1:]):
            i2 = i + _i2 + 1
            if n2 - n <= 3:
                m[i][i2] = 1
            elif n2 - n > 3:
                break
    return m


def debug_matrix(mat, nums):
    print(mat)
    for i in range(len(nums)):
        for i2 in range(len(nums)):
            if mat[i][i2] == 1:
                print(f'{nums[i]} -> {nums[i2]}')
    input()


def count_paths(adj_matr, nums):
    min_jumps = int((max(nums) - min(nums)) / 3) - 1
    m = np.linalg.matrix_power(adj_matr, min_jumps)
    total_paths = 0
    while True:
        paths_n = sum(m[np.ix_([0, 1], [-1])])
        total_paths += paths_n
        min_jumps += 1
        m = np.linalg.matrix_power(adj_matr, min_jumps)
        if min_jumps == len(nums) + 1:
            break
    return total_paths


def main():
    nums = sorted(read_file())
    adj_matr = create_adjacency_matrix(nums)
    print(int(count_paths(adj_matr, nums)[0]))


if __name__ == '__main__':
    main()
