from q15.shared import read_file

target_turn = 2020


def get_spoken_number(spoken_numbers, turn):
    last_spoken_number = spoken_numbers[-1]
    if spoken_numbers.count(last_spoken_number) == 1:
        next_number = 0
    else:
        last_occurances = [i for i, v in enumerate(spoken_numbers) if v == last_spoken_number]
        diff = last_occurances[-1] - last_occurances[-2]
        next_number = diff

        if diff == 1:
            next_number = 1

    print(turn, last_spoken_number, spoken_numbers.count(last_spoken_number) == 1, next_number)
    return next_number


def main():
    starting_numbers = read_file()
    spoken_numbers = starting_numbers
    turn = len(starting_numbers) + 1
    while turn <= target_turn:
        next_number = get_spoken_number(spoken_numbers, turn)
        spoken_numbers.append(next_number)
        turn += 1
    print(spoken_numbers[0:10])
    print(turn)
    print(spoken_numbers.pop())







if __name__ == '__main__':
    main()
