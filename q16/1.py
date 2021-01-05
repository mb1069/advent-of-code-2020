from q16.shared import read_file


def find_invalid_values(rules, ticket):
    rule_funcs = list(rules.values())
    for v in ticket:
        if not any([r(v) for r in rule_funcs]):
            return v
    return 0


def main():
    rules, your_ticket, other_tickets = read_file()

    total_invalid_values = 0
    for ticket in other_tickets:
        invalid_values = find_invalid_values(rules, ticket)
        total_invalid_values += invalid_values
    print(total_invalid_values)


if __name__ == '__main__':
    main()
