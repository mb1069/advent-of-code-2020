from curses.ascii import isalnum

from q19.shared import read_file
import re

numbers = [str(i) for i in range(0, 10)]


class Expr:
    def __init__(self, expr, is_or=True):
        self.children = []


def rule_to_regex(rules, rule):
    # Regex-based solution, intractable for test case
    i2 = 0
    while any([c.isnumeric() for c in rule]):
        # Get index of first subrule
        ref_i = [i for i, c in enumerate(rule) if c.isnumeric()][0]
        rule_ref = rule[ref_i]
        subrule = rules[rule_ref]

        if '|' in subrule:
            subrule = list('(?:') + subrule + [')']

        if isinstance(subrule, str):
            subrule = [subrule]
        rule = rule[0:max(0, ref_i)] + subrule + rule[ref_i + 1:]

        i2 += 1
        print('Iter', i2, len(rule), len([i for i, c in enumerate(rule) if c.isnumeric()]))
        print('Subrule', rule_ref + ':', ' '.join(rules[rule_ref]))
        print('Current rule', ' '.join(rule))
    rule = ''.join(rule)
    return f'({rule})'


def main():
    rules, messages = read_file()
    new_rules = {r: rule_to_regex(rules, v) for r, v in rules.items() if r == '0'}
    print(new_rules['0'])
    total = 0
    for m in messages:
        res = re.findall(new_rules['0'], m)
        print(m, res)
        if len(res) == 1 and res[0] == m:
            total += 1
    print(total)
    # longest_match = sorted(res, key=len, reverse=True)[0]
    # print(m, longest_match, m in res)


if __name__ == '__main__':
    main()
