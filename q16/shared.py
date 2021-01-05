import os
import re


class Rule:
    def __init__(self, name, min1, min2, max1, max2):
        self.name = name
        self.min1 = min1
        self.min2 = min2
        self.max1 = max1
        self.max2 = max2

        self.range = (max2 - min2) + (max1 - min1)
        self.possible_cols = set()

    def __call__(self, val):
        return (self.min1 <= val <= self.max1) or (self.min2 <= val <= self.max2)


def process_ticket(string):
    return list(map(int, string.split(',')))


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        lines = f.readlines()
    rules = dict()

    store_your_ticket = False
    store_other_tickets = False
    your_ticket = None

    other_tickets = []
    for l in lines:
        m = re.findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', l)
        if len(m):
            name, min1, max1, min2, max2 = m[0]
            min1, max1, min2, max2 = list(map(int, [min1, max1, min2, max2]))
            name = f'{name} {min1}-{max1} {min2}-{max2}'
            rules[name] = Rule(name, min1, min2, max1, max2)
            if 'departure' in name:
                print('RULE', name)

        elif store_your_ticket and ',' in l:
            your_ticket = process_ticket(l)
            store_your_ticket = False
        elif 'your ticket' in l:
            store_your_ticket = True

        elif store_other_tickets and ',' in l:
            ticket = process_ticket(l)
            other_tickets.append(ticket)
        elif 'nearby tickets' in l:
            store_other_tickets = True

    return rules, your_ticket, other_tickets
