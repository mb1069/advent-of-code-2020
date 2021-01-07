import os


def read_file():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    rules = dict()
    messages = []
    with open(filepath) as f:
        for l in f:
            l = l.strip()
            if not len(l):
                continue
            if ':' in l:
                rule_num, rule = l.split(':')
                rule = rule.strip()

                if len(rule) == 3 and rule.count('"') == 2:
                    rule = rule[1:2]
                else:
                    rule = rule.split(' ')
                rules[rule_num] = rule
            else:
                messages.append(l)

    return rules, messages
