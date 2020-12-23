import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        txt = f.readlines()
    return txt


def read_rules():
    lines = read_file()
    rules = []
    for l in lines:
        origin, targets = l.split('contain')
        if 'no other bags' in targets:
            continue
        targets = targets.split(',')
        origin_color = origin.replace(' bags ', '').strip()
        for t in targets:
            t = t.strip().split(' ')
            count = t[0]
            target_color = ' '.join(t[1:3])

            rule = [origin_color, count, target_color]
            rules.append(rule)
    return rules


def construct_graph(rules):
    graph = dict()
    for origin, count, target in rules:
        if origin not in graph.keys():
            node = Node(origin)
            graph[origin] = node
        else:
            node = graph[origin]
        node.add_contains(count, target)

        if target not in graph.keys():
            target_node = Node(target)
            graph[target] = target_node
        else:
            target_node = graph[target]
        target_node.add_contained_by(origin)
    return graph


class Node:
    def __init__(self, name):
        self.name = name
        self.contains = dict()
        self.contained_by = set()

    def add_contains(self, count, target):
        self.contains[target] = int(count)

    def add_contained_by(self, origin):
        self.contained_by.add(origin)

    def __repr__(self):
        return str(list(self.contains.keys()))