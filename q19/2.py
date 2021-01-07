import copy
from curses.ascii import isalnum

from q19.shared import read_file
import re

numbers = [str(i) for i in range(0, 10)]


class Expr:
    def __init__(self, expr, rules, is_or=False):
        self.children = []
        self.is_or = False

        if expr == ['8']:
            self.is_or = True
            self.children.append(Expr('42', rules))
            self.children.append(self)
            return

        print(expr)

        if len(expr) == 1:
            expr = rules[expr[0]]

        if '|' in expr:
            self.is_or = True
            i = expr.index('|')
            subrule1 = expr[0:i]
            subrule2 = expr[i + 1:]
            if ' '.join(subrule1) == '1 24':
                print('help')
            # print(expr, 'OR', '->', ' '.join(subrule1), ' '.join(subrule2))
            self.children.append(Expr(subrule1, rules))
            self.children.append(Expr(subrule2, rules))

        else:
            for c in expr:
                if c.isnumeric():
                    if not isinstance(c, list):
                        c = [c]
                    child = Expr(c, rules)
                else:
                    child = Literal(c)
                self.children.append(child)

    def match(self, chars):
        # Wrapper method to enforce exact match (no remaining characters)
        valid, remaining_chars = self._match(chars)
        return valid and len(remaining_chars) == 0

    def _match(self, chars):
        if self.is_or:
            return self._match_or(chars)
        for c in self.children:
            matches, chars = c._match(chars)
            if not matches:
                return False, ''

        return True, chars

    def _match_or(self, chars):
        final_chars = copy.deepcopy(chars)
        for c in self.children:
            matches, final_chars = c._match(chars)
            if matches:
                return matches, final_chars
        return False, final_chars


class Literal:
    def __init__(self, val):
        self.val = val

    def _match(self, chars):
        if len(chars) == 0:
            return False, ''
        return chars[0] == self.val, chars[1:]


def rule_to_tree(rules, rule):
    tree = Expr(rule, rules)
    return tree


def rule_to_regex(rules, rule, is_subrule=False):
    visited_11_count = 0
    # Regex-based solution, messy for part 2
    i2 = 0
    while any([c.isnumeric() for c in rule]):
        # Get index of first subrule
        ref_i = [i for i, c in enumerate(rule) if c.isnumeric()][0]
        rule_ref = rule[ref_i]
        subrule = rules[rule_ref]
        if rule_ref == '42':
            print(' ')
        if '|' in subrule:
            subrule = list('(?:') + subrule + [')']

        if isinstance(subrule, str):
            subrule = [subrule]


        subrule = [('a' if c == '12' else c) for c in subrule]
        subrule = [('b' if c == '57' else c) for c in subrule]
        rule = rule[0:max(0, ref_i)] + subrule + rule[ref_i + 1:]

        i2 += 1
        print('Iter', visited_11_count, i2, len(rule), len([i for i, c in enumerate(rule) if c.isnumeric()]))
        print('Subrule', rule_ref + ':', ' '.join(rules[rule_ref]))

    rule = ''.join(rule)
    if is_subrule:
        return rule
    else:
        return f'({rule})'


def main():
    rules, messages = read_file()

    # Really naive solution, assume that no more than 10 repeats occur
    # Something to come back to...
    rule_8 = '42'
    for i in range(2, 10):
        rule_8 += ' | ' + ' '.join(['42'] * i)
    rules['8'] = rule_8.split(' ')

    rule_11 = '42 31'
    rule_11_tmp = '42 i 31'
    tmp = rule_11_tmp
    for i in range(0, 10):
        tmp = tmp.replace('i', rule_11_tmp)

        rule_11 += ' | ' + tmp.replace('i ', '')
    rules['11'] = rule_11.split(' ')

    rule = rule_to_regex(rules, rules['0'])
    # 374 394
    total = 0
    for m in messages:
        # match = tree.match(m)
        match = sorted(re.findall(rule, m), key=len, reverse=True)
        print(m, match)
        if len(match) and match[0] == m:
            total += 1
    print(total)

    # longest_match = sorted(res, key=len, reverse=True)[0]
    # print(m, longest_match, m in res)


if __name__ == '__main__':
    main()
