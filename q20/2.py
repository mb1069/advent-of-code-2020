from itertools import product

import numpy as  np
from q20.shared import read_file, greedy_solve

monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""


def preprocess_monster():
    txt_rows = list(filter(bool, monster.split('\n')))
    int_rows = np.array([list(r.replace(' ', '0').replace('#', '1')) for r in txt_rows]).astype(int)
    return int_rows


def find_monster(final_img, monster_pattern):
    i_shape = final_img.shape
    m_shape = monster_pattern.shape
    x_min, y_min = 0, 0
    x_max = i_shape[0] - m_shape[0]
    y_max = i_shape[1] - m_shape[1]
    for x, y in product(range(x_min, x_max), range(y_min, y_max)):
        sub_img = final_img[x:x + m_shape[0], y:y + m_shape[1]]
        if np.array_equal(sub_img & monster_pattern, monster_pattern):
            print('Found one!', x, y)
            yield x, y


def iter_arrangement():
    for r in range(0, 4):
        for t in [False, True]:
            yield r, t


def main():
    tiles = read_file()
    tiles = {t: np.array(v) for t, v in tiles.items()}

    solution = greedy_solve(tiles)
    final_img = solution.get_final_image()

    monster_template = preprocess_monster()

    solutions = None
    for r, t in iter_arrangement():
        tmp_img = np.copy(final_img)
        tmp_img = solution.rotate(tmp_img, r)
        tmp_img = solution.flip(tmp_img, t)
        print(r, t, '\n')
        for r in final_img:
            print(''.join(r.astype(str)).replace('0', '.').replace('1', '#'))
        solutions = list(find_monster(tmp_img, monster_template))
        if len(solutions) > 0:
            break

    if len(solutions) == 0:
        print('Failed')
        quit()

    final_img = tmp_img
    for x, y in solutions:
        final_img[x:x + monster_template.shape[0], y:y + monster_template.shape[1]] -= monster_template

    print(final_img.sum())


if __name__ == '__main__':
    main()
