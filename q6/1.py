from q6.shared import read_file


def main():
    groups = read_file()
    groups = [len(set(g.replace('\n', ''))) for g in groups]
    print(sum(groups))


if __name__ == '__main__':
    main()
