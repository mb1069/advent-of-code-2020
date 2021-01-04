from q11.shared import read_file, GameOfAirports


def main():
    seating = read_file()

    game = GameOfAirports()

    final_seating = game.evolve_seating(seating)

    c = game.count_occupied_seats(final_seating)
    print(c)


if __name__ == '__main__':
    main()
