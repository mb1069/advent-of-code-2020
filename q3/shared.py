import os


def read_map():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        return [l.strip() for l in f.readlines()]


def print_position(tree_map, position):
    from copy import deepcopy
    tmp = deepcopy(tree_map)

    l = tmp[position[1]]
    l = list(l)
    l[position[0]] = '@'
    tmp[position[1]] = l

    for l in tmp:
        print(''.join(l))
    print(' ')


def step(position, slope):
    return [position[0] + slope[0], position[1] + slope[1]]


def is_tree(tree_map, position):
    x, y = position
    return tree_map[y][x] == '#'


def correct_position(position, width):
    position[0] = divmod(position[0], width)[1]
    return position


def count_trees(tree_map, start_position, slope):
    tree_count = 0
    bottom = len(tree_map) - 1
    width = len(tree_map[0])
    position = start_position

    while position[1] < bottom:
        position = step(position, slope)
        position = correct_position(position, width)

        if is_tree(tree_map, position):
            tree_count += 1
        print_position(tree_map, position)

    return tree_count