from q3.shared import read_map, count_trees


def main():
    tree_map = read_map()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    start_position = (0, 0)

    product_tree_counts = 1
    for slope in slopes:
        tree_count = count_trees(tree_map, start_position, slope)
        product_tree_counts *= tree_count
    print(product_tree_counts)


if __name__ == '__main__':
    main()
