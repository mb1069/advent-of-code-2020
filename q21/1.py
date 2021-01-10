from q21.shared import read_file, get_non_allergic_ingredients


def main():
    food_list = read_file()
    get_non_allergic_ingredients(food_list)


if __name__ == '__main__':
    main()
