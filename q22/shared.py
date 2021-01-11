import os
import re


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(filepath) as f:
        data = f.read()
    player_data = re.findall(r'(.+):\n([\d\n]+)+', data)

    players = [Player(d[0], list(map(int, filter(bool, d[1].split('\n'))))) for d in player_data]

    return players
