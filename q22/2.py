from copy import deepcopy
from collections import deque
from q22.shared import read_file


class RecursiveCombat:
    def __init__(self, d1, d2):
        self.d1 = deque(d1)
        self.d2 = deque(d2)
        self.visited = set()

    def get_state(self):
        player_decks = [','.join(list(map(str, d))) for d in [self.d1, self.d2]]
        return '-'.join(player_decks)

    def state_check(self):
        state = self.get_state()
        if state in self.visited:
            return True
        self.visited.add(state)

    def round(self):
        if self.state_check():
            return 'p1'
        c1, c2 = self.d1.popleft(), self.d2.popleft()
        if c1 <= len(self.d1) and c2 <= len(self.d2):
            subgame = RecursiveCombat(list(self.d1)[:c1], list(self.d2)[:c2])
            winner = subgame.play()
        else:
            if c1 > c2:
                winner = 'p1'
            else:
                winner = 'p2'

        if winner == 'p1':
            self.d1.append(c1)
            self.d1.append(c2)
        else:
            self.d2.append(c2)
            self.d2.append(c1)
        if not (self.d1 and self.d2):
            return winner

    def play(self):
        while True:
            winner = self.round()
            if winner:
                return winner

    def score(self, name):
        if name == 'p1':
            deck = self.d1
        else:
            deck = self.d2
        score = 0
        for i, card in enumerate(reversed(deck)):
            print()
            score += (card * (i + 1))
        return score


def main():
    players = read_file()

    game = RecursiveCombat(*[p.deck for p in players])

    winner = game.play()

    score = game.score(winner)
    print(score)

if __name__ == '__main__':
    main()
