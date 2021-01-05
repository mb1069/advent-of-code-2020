from q16.shared import read_file


def is_invalid_ticket(rules, ticket):
    rule_funcs = list(rules.values())
    for v in ticket:
        if not any([r(v) for r in rule_funcs]):
            return True
    return False


def main():
    rules, your_ticket, other_tickets = read_file()
    print('Starting tickets', len(other_tickets))
    other_tickets = list(filter(lambda t: not (is_invalid_ticket(rules, t)), other_tickets))
    print('Filtered tickets', len(other_tickets))

    rule_values = dict()
    for i, v in enumerate(range(len(rules))):
        rule_values[i] = {t[i] for t in other_tickets}

    lst_rules = list(rules.values())

    # Find all potential columns for each rule
    for rule in lst_rules:
        for i, rv in rule_values.items():
            if all([rule(v) for v in rv]):
                rule.possible_cols.add(i)

    assigned_rules = dict()
    # Greedy approach, sort by increasing number of possible_columns
    lst_rules = sorted(lst_rules, key=lambda r: len(r.possible_cols))
    while len(assigned_rules) != len(rules):
        rule = lst_rules.pop(0)
        if len(rule.possible_cols) != 1:
            print('Multiple combinations possible...')
            quit()

        col = rule.possible_cols.pop()
        assigned_rules[rule.name] = col
        print('Assigning', rule.name, col)

        for rule in lst_rules:
            rule.possible_cols.remove(col)

    all_cols_compatible = True
    for rule_name, col in assigned_rules.items():
        rule = rules[rule_name]
        all_tickets_valid = all([rule(t[col]) for t in other_tickets])
        if not all_tickets_valid:
            all_cols_compatible = False
            break
    print('Are all columns assigned correctly: ', all_cols_compatible, '\n')

    departure_rules = {k: v for k, v in assigned_rules.items() if 'departure' in k}

    product = 1

    for rule_name, rule_col in departure_rules.items():
        ticket_val = your_ticket[rule_col]
        rule = rules[rule_name]
        product *= ticket_val
        print(rule.name, ticket_val)
    print(product)


if __name__ == '__main__':
    main()
