from collections import deque, UserList

from q23.shared import read_file



class Circle:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self.data[i]
        else:
            return self.data[i % len(self)]

    def __len__(self):
        return len(self.data)

    def index(self, val):
        for i in range(0, len(self)):
            if self[i] == val:
                return i
        return None

    def pop_slice(self, s):
        res = []
        for i in range(s.start, s.stop):
            res.append(self.data.pop(s.start + 1))
        return res

    def ins_slice(self, i, data):
        for d in reversed(data):
            self.data.insert(i, d)

    def __iter__(self):
        for i in range(len(self)):
            yield self.data[i]

    def rotate(self, n):
        for _ in range(n):
            self.data.append(self.data.pop(0))


class Game:
    n_pickup = 3

    def __init__(self, cups):
        self.cups = Circle(cups)

    def play_n_turns(self, n):
        pick_i = 0
        for i in range(1, n + 1):
            print(f'\n-- move {i} --')
            pick_i = self.play_turn(pick_i)

    def play_turn(self, pick_i):
        if pick_i > 4:
            self.cups.rotate(4)
            pick_i -= 4
        cup_str = list(map(str, self.cups))
        cup_str[pick_i] = f'({cup_str[pick_i]})'
        print(f'cups: {" ".join(cup_str)}')
        current_cup_label = self.cups[pick_i]
        pickup = self.cups.pop_slice(slice(pick_i, pick_i + self.n_pickup))
        print(f'pick up: {", ".join(list(map(str, pickup)))}')
        print(f'cups: {" ".join(list(map(str, self.cups)))}')
        # print(f'cups: ({self.cups[0]}) {" ".join(list(map(str, self.cups[1:])))}')
        dest_label = current_cup_label - 1

        while dest_label in pickup or dest_label <= 0:
            dest_label -= 1
            if dest_label <= 0:
                dest_label = 9
        dest_i = self.cups.index(dest_label) + 1

        print(f'destination: {dest_label}')
        self.cups.ins_slice(dest_i, pickup)
        if dest_i <= pick_i:
            pick_i += self.n_pickup
        return pick_i + 1

    def rotate_n_first(self, n):
        i = self.cups.index(n)
        self.cups.rotate(i)


def main():
    cups = read_file()

    game = Game(cups)

    game.play_n_turns(100)

    game.rotate_n_first(1)

    final_state = ''.join(list(map(str, game.cups.data[1:])))
    print(final_state)


if __name__ == '__main__':
    main()
