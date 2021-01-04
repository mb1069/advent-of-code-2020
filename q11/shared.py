import copy
import os

occupied = '#'
empty = 'L'
floor = '.'


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        txt = f.readlines()
    rows = [list(t.strip()) for t in txt]
    return rows


class GameOfAirports:
    def __init__(self):
        pass

    def get_new_seat_type(self, seating, x, y):
        adj_seats = self.get_adjacent_seat_count(seating, x, y)
        current_seat = seating[y][x]
        if current_seat == empty and adj_seats == 0:
            return occupied
        if adj_seats >= 4 and current_seat == occupied:
            return empty
        return current_seat

    @staticmethod
    def get_adjacent_seat_count(seating, x, y):
        seating_max_x = len(seating[0])
        seating_max_y = len(seating)

        xcoords = [-1, 0, 1]
        ycoords = [-1, 0, 1]

        surrounding_seats = []
        for mx in xcoords:
            for my in ycoords:
                if mx == 0 and my == 0:
                    continue
                seat_x = mx + x
                seat_y = my + y
                if not (0 <= seat_x < seating_max_x and 0 <= seat_y < seating_max_y):
                    continue
                else:
                    surrounding_seats.append(seating[seat_y][seat_x])
        return len(list(filter(lambda s: s == occupied, surrounding_seats)))

    def next_seating(self, seating):
        new_seating = copy.deepcopy(seating)
        for y in range(len(new_seating)):
            for x in range(len(new_seating[0])):
                new_seat = self.get_new_seat_type(seating, x, y)
                new_seating[y][x] = new_seat
        return new_seating

    def evolve_seating(self, seating):
        current_seating = seating
        i = 0
        while True:
            print(i)
            i += 1
            new_seating = self.next_seating(copy.deepcopy(current_seating))
            if current_seating == new_seating:
                return new_seating
            current_seating = new_seating

    @staticmethod
    def count_occupied_seats(seating):
        total_occupied_seats = 0
        for row in seating:
            row_occupied_seats = len([s for s in row if s == occupied])
            total_occupied_seats += row_occupied_seats
        return total_occupied_seats


def print_seating(seating):
    for r in seating:
        print(''.join(r))
    print('\n')
