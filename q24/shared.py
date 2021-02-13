import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        tiles = [l.strip() for l in f.readlines()]
    return tiles


direction_step = {
    'e': (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'w': (-1, 1, 0),
    'nw': (0, 1, -1),
    'ne': (1, 0, -1),
}
direction_count = {k: 0 for k in direction_step.keys()}


def step_direction(coords, diff):
    return tuple(x + y for x, y in zip(coords, diff))


class TileWalk:
    def __init__(self, directions):
        self.coords = (0, 0, 0)
        self.directions = directions

    def find_tile(self):
        while len(self.directions):
            self.step()
        return ','.join(map(str, self.coords))

    def step(self):
        for direction, diff in direction_step.items():
            if self.directions.startswith(direction):
                direction_count[direction] += 1
                self.directions = self.directions[len(direction):]
                self.coords = step_direction(self.coords, diff)
                break


class TileSet:
    def __init__(self, tiles):
        self.tiles = tiles

    def add(self, t):
        if t not in self.tiles:
            self.tiles.append(t)

    def __contains__(self, t):
        return t in self.tiles

    def __len__(self):
        return len(self.tiles)

    def __iter__(self):
        return iter(self.tiles)

    def __repr__(self):
        return str(self.tiles)


class HexGameOfLife:
    def __init__(self, black_tiles):
        self.black_tiles = TileSet(black_tiles)

    def play(self, n):
        print(f'Start: {len(self.black_tiles)}')
        for i in range(0, n):
            self.evolve()
            print(f'Day {i+1}: {len(self.black_tiles)}')

    def evolve(self):
        current_white = TileSet([])
        next_black = TileSet([])
        # print(self.black_tiles)
        for t in self.black_tiles:
            bordering_tiles = get_bordering_tiles(t)
            count_bordering_black = 0
            for bt in bordering_tiles:
                if bt not in self.black_tiles:
                    current_white.add(bt)
                else:
                    count_bordering_black += 1
            if count_bordering_black in (1, 2):
                next_black.add(t)
            # print('Tile', t, count_bordering_black)
        # print('WSet', current_white)
        for w in current_white:
            bordering_tiles = get_bordering_tiles(w)
            count_tiles = sum([1 for bt in bordering_tiles if bt in self.black_tiles])
            if count_tiles == 2:
                next_black.add(w)
                # print('WTile', w, count_tiles)
        self.black_tiles = next_black


def get_bordering_tiles(coords):
    return [step_direction(coords, diff) for diff in direction_step.values()]
