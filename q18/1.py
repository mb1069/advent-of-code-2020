from q18.shared import read_file, Problem


def main():
    problems = read_file()
    total = 0
    for p_txt in problems:
        p = Problem(p_txt.split(' '))
        total += p.solve()
    print(total)


if __name__ == '__main__':
    main()
