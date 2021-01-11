from q22.shared import read_file


class Game:
    def __init__(self, players):
        self.players = players
        self.turn = 1

    def game_finished(self):
        return any([len(p.deck) == 0 for p in self.players])

    def select_winner(self):
        player_deck_sizes = [len(p.deck) for p in self.players]
        print(player_deck_sizes)
        max_size = max(player_deck_sizes)
        winner = self.players[player_deck_sizes.index(max_size)]
        print(f'Winner is {winner.name}')
        print(f'Winner is {winner.deck}')
        return winner

    def play_turn(self):
        cards = [p.deck.pop(0) for p in self.players]
        print(f'Turn {self.turn}: {cards}')
        winner = self.players[cards.index(max(cards))]
        winning_order = sorted(cards, reverse=True)
        winner.deck.extend(winning_order)

        self.turn += 1

    def play(self):
        while not self.game_finished():
            self.play_turn()
        return self.select_winner()

    def score(self, winner):
        score = 0
        for i, card in enumerate(reversed(winner.deck)):
            print()
            score += (card * (i + 1))
        return score


def main():
    players = read_file()

    game = Game(players)

    winner = game.play()

    print(winner.name)
    print(f'Final score: {game.score(winner)}')


if __name__ == '__main__':
    main()
