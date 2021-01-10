import copy
import os
import re
from itertools import product

import numpy as np


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    tiles = dict()
    t_num = None
    tile_data = []

    with open(filepath) as f:
        for l in f:
            l = l.strip()
            if 'Tile' in l:
                t_num = int(re.findall(r'Tile (\d+):', l)[0])
            elif t_num is not None and len(l) > 0:
                l = list(l.replace('.', '0').replace('#', '1'))
                l = list(map(int, l))
                tile_data.append(l)
            elif len(l) == 0:
                tiles[t_num] = tile_data
                tiles[t_num] = tile_data
                t_num = None
                tile_data = []
        if t_num is not None and len(tile_data) > 0:
            tiles[t_num] = tile_data

    return tiles


def chunk_lst(lst, n):
    i = 0
    while i + n <= len(lst):
        yield lst[i:i + n]
        i += n


class Solution:
    def __init__(self, tiles, order, rotation, flips, width):
        self.tiles = tiles
        self.order = order
        self.rotations = rotation
        self.flips = flips
        self.width = width

        self.matching_fits_hist = []

        self.compatible_fits = []

    def check_all(self):
        valid = True
        for i, t in enumerate(self.order[0:-1]):
            x, y = self.i_to_xy(i)
            if not self.check_right(x, y):
                valid = False
                break

            if not self.check_down(x, y):
                valid = False
                break
        return valid

    def check_is_valid(self, rot, flip):
        self.rotations.append(rot)
        self.flips.append(flip)

        last_i = len(self.order) - 1
        x, y = self.i_to_xy(last_i)

        valid = True
        if x > 0:
            valid = self.check_right(x - 1, y)
        if y > 0:
            valid = self.check_down(x, y - 1)
        self.rotations.pop()
        self.flips.pop()
        return valid

    def get_final_image(self):
        tile_data = [self.get_final_tile(i) for i in range(len(self.order))]
        tile_data = [t[1:9, 1:9] for t in tile_data]
        chunked_tiles = list(chunk_lst(tile_data, self.width))
        rows = [np.hstack(row_tiles) for row_tiles in chunked_tiles]
        return np.vstack(rows)

    def get_final_tile(self, i):
        x, y = self.i_to_xy(i)
        return self.get_config_tile(x, y)

    def get_config_tile(self, x, y):
        i = self.xy_to_i(x, y)
        tile_id = self.order[i]
        pixels = self.tiles[tile_id]
        pixels = self.flip(pixels, self.flips[i])
        pixels = self.rotate(pixels, self.rotations[i])
        return pixels

    @staticmethod
    def flip(pixels, enabled):
        if enabled:
            return pixels.T
        return pixels

    @staticmethod
    def rotate(pixels, k):
        return np.rot90(pixels, k=k)

    def check_right(self, x, y):
        if self.xy_to_i(x + 1, y) > len(self.order) - 1:
            return True

        left = self.get_config_tile(x, y)
        right = self.get_config_tile(x + 1, y)
        left_square_edge = left[:, -1]
        right_square_edge = right[:, 0]
        score = int(np.array_equal(left_square_edge, right_square_edge))
        return score

    def check_down(self, x, y):
        if self.xy_to_i(x, y + 1) > len(self.order) - 1:
            return True

        top = self.get_config_tile(x, y)
        bottom = self.get_config_tile(x, y + 1)
        bottom_edge = top[-1, :]
        top_edge = bottom[0, :]
        score = int(np.array_equal(bottom_edge, top_edge))
        return score

    def i_to_xy(self, i):
        x = i % self.width
        y = i // self.width
        return x, y

    def xy_to_i(self, x, y):
        return x + (y * self.width)

    def fit_tile(self, tile_id):
        self.compatible_fits = []
        self.order.append(tile_id)
        # print(f'Trying {self.order} {len(self.rotations)} {len(self.flips)}')
        for r in range(0, 4):
            for t in [False, True]:
                if self.check_is_valid(r, t):
                    self.compatible_fits.append((r, t))

        self.order.pop()
        if len(self.compatible_fits) > 0:
            # print(f'Found {self.compatible_fits} for {tile_id}')
            return True
        return False

    def next(self, new_tile):
        # print(f'Setting next {new_tile}')
        self.order.append(new_tile)
        rot, flip = self.compatible_fits.pop()
        self.rotations.append(rot)
        self.flips.append(flip)
        self.matching_fits_hist.append(copy.deepcopy(self.compatible_fits))
        self.compatible_fits = []

    def try_alt(self):
        rot, flip = self.compatible_fits.pop()
        self.rotations.pop()
        self.flips.pop()
        self.rotations.append(rot)
        self.flips.append(flip)

    def revert(self):
        # print(f'R1: {self.order} {self.rotations} {self.flips} {self.matching_fits_hist} {self.compatible_fits}')
        removed_tile = self.order.pop()
        # print(f'Reverted {removed_tile}')
        self.compatible_fits = self.matching_fits_hist.pop()
        self.rotations.pop()
        self.flips.pop()
        # print(self.order)
        # print(self.rotations)
        # print(self.flips)
        assert len(self.order) == len(self.rotations)
        assert len(self.order) == len(self.flips)
        if not len(self.compatible_fits) and len(self.order) > 1:
            return [removed_tile] + self.revert()

        # print(f'R2: {self.order} {self.rotations} {self.flips} {self.matching_fits_hist} {self.compatible_fits}')
        return [removed_tile]


def gen_init_solution(tiles, starting_tile, starting_rotation, starting_flip):
    order = [starting_tile]
    rotations = [starting_rotation]
    flips = [starting_flip]
    width = int(np.sqrt(len(tiles.keys())))
    return Solution(tiles, order, rotations, flips, width)


def greedy_solve(tiles):
    # 1 min execution time for small solutions
    ref_tile_ids = set(tiles.keys())
    i = 0

    for starting_tile, starting_rotation, starting_flip in list(product(ref_tile_ids, range(0, 4), [True, False])):
        remaining_tiles = copy.deepcopy(ref_tile_ids)
        remaining_tiles.remove(starting_tile)
        i += 1
        solution = gen_init_solution(tiles, starting_tile, starting_rotation, starting_flip)

        blacklisted_at_index = dict()
        attempted_tiles = set()

        while len(remaining_tiles):
            # print(solution.order)
            pick = remaining_tiles.pop()

            # Avoid retrying previous solutions
            if len(solution.order) in blacklisted_at_index and pick in blacklisted_at_index[len(solution.order)]:
                attempted_tiles.add(pick)
                # print(f'{pick} was in blacklist.')
                continue

            if solution.fit_tile(pick):
                solution.next(pick)
                remaining_tiles = remaining_tiles.union(attempted_tiles)
                attempted_tiles = set()
                continue
            else:
                attempted_tiles.add(pick)

            if len(remaining_tiles) == 0:
                try:
                    # print('No solutions, trying alts')
                    solution.try_alt()
                except IndexError:
                    # print('Out of alts, reverting...')
                    try:
                        tile_ids = solution.revert()
                    except IndexError:
                        # print('Nothing to revert, giving up...')
                        break
                    remaining_tiles = remaining_tiles.union(set(tile_ids))
                    if len(solution.order) not in blacklisted_at_index:
                        blacklisted_at_index[len(solution.order)] = []
                    blacklisted_at_index[len(solution.order)].extend(tile_ids)

        if len(solution.order) == len(ref_tile_ids):
            # Reset for next starting config
            print('Found Arrangement!')
            print(solution.order)
            return solution
        else:
            # print('Restarting\n')
            pass
    print(f'Tried {i} times.')
    combs = len(ref_tile_ids) * 2 * 4
    print(f'Starting combinations = {combs}')
