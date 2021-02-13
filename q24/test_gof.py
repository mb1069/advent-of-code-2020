import unittest
from itertools import combinations

from q24.shared import HexGameOfLife, get_bordering_tiles


class TestGameOfLife(unittest.TestCase):
    def test_isolated_black(self):
        starting_tiles = [(0, 0, 0)]
        hgol = HexGameOfLife(starting_tiles)
        hgol.evolve()
        assert len(hgol.black_tiles) == 0

    def test_crowded_black(self):
        starting_tile = (0, 0, 0)
        bordering_tiles = get_bordering_tiles(starting_tile)
        for starting_set in combinations(bordering_tiles, 3):
            starting_set = list(starting_set)
            starting_set.append(starting_tile)
            hgol = HexGameOfLife(starting_set)
            hgol.evolve()
            assert (0, 0, 0) not in hgol.black_tiles

    def test_new_white(self):
        starting_tile = (0, 0, 0)
        bordering_tiles = get_bordering_tiles(starting_tile)
        for starting_set in combinations(bordering_tiles, 2):
            starting_set = list(starting_set)
            hgol = HexGameOfLife(starting_set)
            hgol.evolve()
            assert (0, 0, 0) in hgol.black_tiles

            if starting_set[0] in get_bordering_tiles(starting_set[1]):
                print('bordering')
                expected_total = 4
            else:
                if tuple(-s for s in starting_set[0]) == starting_set[1]:
                    expected_total = 1
                else:
                    expected_total = 2
            print(hgol.black_tiles)
            print(starting_set, len(hgol.black_tiles))
            assert len(hgol.black_tiles) == expected_total
            print('\n')


if __name__ == '__main__':
    unittest.main()
