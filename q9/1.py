from q9.shared import find_preamble_limit

preamble_length = 25


def main():
    l = find_preamble_limit(preamble_length)
    print(f'First number after preamble:', l)

if __name__ == '__main__':
    main()
