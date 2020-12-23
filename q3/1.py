from q3.shared import read_map, count_trees

start_position = (0, 0)
slope = (3, 1)


def main():
    tree_map = read_map()

    tree_count = count_trees(tree_map, start_position, slope)
    print(tree_count)


if __name__ == '__main__':
    main()
