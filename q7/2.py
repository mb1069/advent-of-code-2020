from q7.shared import read_rules, construct_graph


# Naive solution, OK for this scale of problem but recursive would be better.
def count_bags(graph, origin):
    total = 0
    bags_to_open = [origin]
    while len(bags_to_open):
        opened_bag = bags_to_open.pop()
        node = graph[opened_bag]
        for target, count in node.contains.items():
            for _ in range(count):
                total += 1
                bags_to_open.append(target)
        print(total, opened_bag, bags_to_open)
    print(total)


def main():
    rules = read_rules()
    graph = construct_graph(rules)
    count_bags(graph, 'shiny gold')


if __name__ == '__main__':
    main()
