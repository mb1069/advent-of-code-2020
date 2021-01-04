from q11.shared import read_file, GameOfAirports, empty, occupied, floor, print_seating, empty
import copy

direction_funcs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x + 1, y + 1),
    lambda x, y: (x, y + 1),
    lambda x, y: (x - 1, y + 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x - 1, y - 1),
    lambda x, y: (x, y - 1),
    lambda x, y: (x + 1, y - 1),
]


class GameOfAirportsV3(GameOfAirports):

    @staticmethod
    def get_visible_seats(seating, x, y):

        # disp_seating = copy.deepcopy(seating)
        # disp_seating[y][x] = 'H'
        # print_seating(disp_seating)

        seating_max_x = len(seating[0])
        seating_max_y = len(seating)

        occupied_seats = 0
        for func in direction_funcs:
            f_x, f_y = func(x, y)
            while (0 <= f_x < seating_max_x) and (0 <= f_y < seating_max_y):
                if not (seating[f_y][f_x] == floor):
                    # disp_seating[f_y][f_x] = 'V'
                    occupied_seats += int(seating[f_y][f_x] == occupied)
                    break
                f_x, f_y = func(f_x, f_y)
        # print_seating(disp_seating)
        return occupied_seats

    def get_new_seat_type(self, seating, x, y):
        current_seat = seating[y][x]
        if current_seat == floor:
            return floor
        visible_seats = self.get_visible_seats(seating, x, y)
        # print(visible_seats)
        if current_seat == empty and visible_seats == 0:
            return occupied
        if visible_seats >= 5 and current_seat == occupied:
            return empty
        return current_seat


def main():
    seating = read_file()

    game = GameOfAirportsV3()

    # print(game.get_new_seat_type(seating, 2, 0))
    # quit()
    final_seating = game.evolve_seating(seating)

    c = game.count_occupied_seats(final_seating)
    print(c)


if __name__ == '__main__':
    main()
