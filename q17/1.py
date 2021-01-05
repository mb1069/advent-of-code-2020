from itertools import product

from q17.shared import read_file
import numpy as np


class GameOfLife3D:
    def __init__(self, initial_state):
        self.x = len(initial_state[0])
        self.y = len(initial_state)
        self.z = 1
        self.cube = np.zeros((1, self.y, self.x))
        for y, row in enumerate(initial_state):
            for x, val in enumerate(row):
                if val == '#':
                    self.cube[0][y][x] = 1
        print('Starting cube:')
        print(self.cube)
        print(self.cube.shape, '\n')

    def expand_borders(self):
        x_pad = self.get_x_pad()
        y_pad = self.get_y_pad()
        z_pad = self.get_z_pad()

        npad = (z_pad, y_pad, x_pad)
        print('Updating padding:')
        print(npad)

        print('\t', self.cube.shape)
        self.cube = np.pad(self.cube, pad_width=npad, mode='constant', constant_values=0)
        new_shape = self.cube.shape
        print('\t', new_shape)
        self.z, self.y, self.x = new_shape

    # Always increase padding, quicker than calculating whether a cell will become active or not
    def get_x_pad(self):
        return 1, 1

    def get_y_pad(self):
        return 1, 1

    def get_z_pad(self):
        return 1, 1

    def get_sum_adjacent_cells(self, x, y, z):
        min_z = max(z - 1, 0)
        max_z = z + 2

        min_y = max(y - 1, 0)
        max_y = y + 2

        min_x = max(x - 1, 0)
        max_x = x + 2

        subcube = self.cube[min_z:max_z, min_y:max_y, min_x:max_x]
        total = subcube.sum() - self.cube[z, y, x]
        return total

    def gen_next_cube(self):
        self.expand_borders()
        newcube = np.zeros((self.z, self.y, self.x))
        zs = list(range(self.z))
        ys = list(range(self.y))
        xs = list(range(self.x))
        for z, y, x in product(zs, ys, xs):
            cube_active = self.cube[z, y, x] == 1
            active_neighbours = self.get_sum_adjacent_cells(x, y, z)
            if cube_active:
                print(x, y, z, active_neighbours)
            if cube_active:
                if 2 <= active_neighbours <= 3:
                    val = 1
                else:
                    val = 0
            else:
                if active_neighbours == 3:
                    val = 1
                else:
                    val = 0
            newcube[z, y, x] = val

        self.cube = newcube
        self.print_cube()

    def print_cube(self):
        for z in range(self.z):
            print(z - (self.z // 2))
            print(self.cube[z, :, :])


def main():
    cube_slice = read_file()

    cube = GameOfLife3D(cube_slice)
    for i in range(0, 6):
        cube.gen_next_cube()
    print(cube.cube.sum())


if __name__ == '__main__':
    main()
