from q12.shared import read_file
import math

direction = {
    0: 'E',
    90: 'N',
    180: 'W',
    270: 'S',
}

class Ship:
    orientation = 0
    x = 0
    y = 0

    def process_instructions(self, instructions):
        for ins in instructions:
            print(ins)
            self.process_instruction(ins)
            print(round(self.x, 2), self.y, direction[self.orientation])
            # input()

    def process_instruction(self, instruction):
        order, order_var = instruction[0], int(instruction[1:])
        if order == 'F':
            self.move_forward(order_var)
        elif order == 'N':
            self.move_north(order_var)
        elif order == 'S':
            self.move_south(order_var)
        elif order == 'E':
            self.move_east(order_var)
        elif order == 'W':
            self.move_west(order_var)
        elif order == 'L':
            self.turn(order_var)
        elif order == 'R':
            self.turn(-order_var)

    def move_forward(self, distance):
        dx = distance * math.cos(math.radians(self.orientation))
        dy = distance * math.sin(math.radians(self.orientation))

        self.x += dx
        self.y += dy

    def move_north(self, distance):
        self.y += distance

    def move_south(self, distance):
        self.y -= distance

    def move_west(self, distance):
        self.x -= distance

    def move_east(self, distance):
        self.x += distance

    def turn(self, ang):
        self.orientation += ang
        if self.orientation >= 360:
            self.orientation -= 360
        elif self.orientation < 0:
            self.orientation += 360

    def get_manhattan(self):
        return round(abs(self.x) + abs(self.y))


def main():
    instructions = read_file()
    s = Ship()
    s.process_instructions(instructions)

    print(s.get_manhattan())


if __name__ == '__main__':
    main()
