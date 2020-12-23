from functools import reduce

from q6.shared import read_file


def process_group(group):
    answers = [set(a) for a in group.split('\n')]
    common_answers = reduce(lambda a, b: a.intersection(b), answers)
    return len(common_answers)


def main():
    total = 0
    groups = read_file()
    for g in groups:
        common_answers = process_group(g)
        total += common_answers
    print(total)


if __name__ == '__main__':
    main()
