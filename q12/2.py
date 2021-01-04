from q12.shared import read_file
import math
import numpy as np

direction = {
    0: 'E',
    90: 'N',
    180: 'W',
    270: 'S',
}


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u.T, v2_u), -1, 1))


class Ship:
    coords = np.zeros((2, ))
    waypoint = np.array([10, 1])

    def process_instructions(self, instructions):
        for ins in instructions:
            self.process_instruction(ins)
            # print(ins)
            # print(self.coords, self.waypoint)
            # input()

    def process_instruction(self, instruction):
        order, order_var = instruction[0], int(instruction[1:])
        if order == 'F':
            self.move_forward(order_var)
        elif order == 'N':
            self.move_waypoint_north(order_var)
        elif order == 'S':
            self.move_waypoint_south(order_var)
        elif order == 'E':
            self.move_waypoint_east(order_var)
        elif order == 'W':
            self.move_waypoint_west(order_var)
        elif order == 'L':
            self.turn(-order_var)
        elif order == 'R':
            self.turn(order_var)

    def move_forward(self, distance):
        self.coords = (self.waypoint * distance).squeeze() + self.coords.squeeze()

    def move_waypoint_north(self, distance):
        self.waypoint[1] += distance

    def move_waypoint_south(self, distance):
        self.waypoint[1] -= distance

    def move_waypoint_west(self, distance):
        self.waypoint[0] -= distance

    def move_waypoint_east(self, distance):
        self.waypoint[0] += distance

    def turn(self, ang):
        ang = math.radians(ang)
        s = math.sin(ang)
        c = math.cos(ang)
        new_x = (self.waypoint[0] * c) + (self.waypoint[1] * s)
        new_y = (self.waypoint[1] * c) - (self.waypoint[0] * s)

        # Still buggy
        self.waypoint = np.array([new_x, new_y])

    def get_manhattan(self):
        return int(abs(self.coords).sum())


def main():
    instructions = read_file()
    s = Ship()
    s.process_instructions(instructions)

    print(s.get_manhattan())


if __name__ == '__main__':
    main()
