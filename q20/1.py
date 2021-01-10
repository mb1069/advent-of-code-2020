from itertools import product

from q20.shared import read_file, greedy_solve
import numpy as np
from functools import reduce


def compute_square(order, width):
    coords = list(product((0, width - 1), repeat=2))
    indices = [x + (y * width) for x, y in coords]
    vals = [order[i] for i in indices]
    prod = reduce(lambda a, b: a * b, vals)
    print(f'Corner vals: {vals}')
    print(f'Total: {prod}')


# for starting_tile in tiles:
# init a solution
# while solution does not contain all tiles

def get_edge_set(tiles):
    edge_sets = dict()
    for id, t in tiles.items():
        top_edge = t[0, :].sum()
        bottom_edge = t[-1, :].sum()
        left_edge = t[:, 0].sum()
        right_edge = t[:, -1].sum()
        edge_sets[id] = {top_edge, bottom_edge, left_edge, right_edge}
    return edge_sets




def main():
    tiles = read_file()
    tiles = {t: np.array(v) for t, v in tiles.items()}

    solution = greedy_solve(tiles)

    compute_square(solution.order, solution.width)


if __name__ == '__main__':
    main()
