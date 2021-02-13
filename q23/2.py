from collections import OrderedDict

from tqdm import trange

DEBUG = False


class Cup:
    def __init__(self, val):
        self.val = val
        self.next = None


class CupCircle:
    def __init__(self, cups):
        self.cup_dict = OrderedDict()
        for i, c in enumerate(cups):
            cup = Cup(c)
            self.cup_dict[c] = cup

        for i, c in enumerate(cups):
            if i + 1 < len(cups):
                self.cup_dict[c].next = self.cup_dict[cups[i + 1]]
            else:
                self.cup_dict[c].next = self.cup_dict[cups[0]]

        self.max_cup = max(cups)
        self.current_cup = self.cup_dict[cups[0]]

        self.num_cups = len(cups)
        self.n_moves = 1

    def print_cups(self, start_cup, label='cups'):
        print(f'{label}: ', end='')
        print(f'({start_cup.val})', end=' ')
        cup = start_cup.next
        while cup is not None and cup.val != self.current_cup.val:
            print(f'{cup.val}', end=' ')
            cup = cup.next
        print('')

    def move(self):
        if DEBUG:
            print(f'-- move {self.n_moves} --')
            self.print_cups(self.current_cup)

        destination = self.current_cup.val - 1
        pickup_cups, pickup_vals = self.take_cups()

        while destination in pickup_vals or destination == 0:
            destination -= 1
            if destination <= 0:
                destination = self.max_cup
        if DEBUG:
            print(f'destination: {destination}')

        destination_cup = self.cup_dict[destination]
        self.insert_cups(destination_cup, pickup_cups)
        self.n_moves += 1

        self.current_cup = self.current_cup.next

    def insert_cups(self, destination_cup, pickup_cups):
        tail = destination_cup.next
        destination_cup.next = pickup_cups
        pickup_tail = pickup_cups.next
        while pickup_tail.next is not None:
            pickup_tail = pickup_tail.next
        pickup_tail.next = tail

    def take_cups(self):
        pickup_start = self.current_cup.next

        pickup_vals = [pickup_start.val]
        pickup_tail = self.current_cup.next
        for i in range(0, 2):
            pickup_tail = pickup_tail.next
            pickup_vals.append(pickup_tail.val)

        self.current_cup.next = pickup_tail.next
        pickup_tail.next = None
        if DEBUG:
            self.print_cups(pickup_start, label='pick up')
        return pickup_start, pickup_vals

    def get_ordering(self, start_cup_val):
        start_cup = self.cup_dict[start_cup_val]

        cup_vals = []
        next_cup = start_cup.next
        while next_cup.val != start_cup_val:
            cup_vals.append(next_cup.val)
            next_cup = next_cup.next

        cups = list(map(str, cup_vals))
        return ''.join(cups)

    def get_cup_sum(self):
        index_cup = self.cup_dict[1]
        print(index_cup.next.val, index_cup.next.next.val)
        return index_cup.next.val * index_cup.next.next.val


start_cups = list(map(int, list('398254716')))

total_cups = 1000000
for i in range(max(start_cups) + 1, total_cups + 1):
    start_cups.append(i)

cc = CupCircle(start_cups)
for i in trange(10000000):
    cc.move()

print(cc.get_cup_sum())
