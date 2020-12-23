from q7.shared import read_rules, construct_graph


def find_origins(graph, target):
    origins = set()
    to_explore = [target]
    while len(to_explore):
        open_node_name = to_explore.pop()
        node = graph[open_node_name]
        contained_by = node.contained_by
        for origin in contained_by:
            origins.add(origin)
            if origin not in to_explore:
                to_explore.append(origin)
    print(len(origins))

def main():
    rules = read_rules()
    graph = construct_graph(rules)
    find_origins(graph, 'shiny gold')


if __name__ == '__main__':
    main()
