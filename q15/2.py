from q15.shared import read_file

target_turn = 30000000
from tqdm import trange


def get_spoken_number(spoken_numbers, last_spoken_number, turn):
    if last_spoken_number not in spoken_numbers:
        next_number = 0
    else:
        last_occurances = spoken_numbers[last_spoken_number]
        next_number = max(last_occurances) - min(last_occurances)

    # print(turn, last_spoken_number, spoken_numbers.count(last_spoken_number) == 1, next_number)
    return next_number


def main():
    starting_numbers = read_file()
    seen_numbers = dict()
    for i, s in enumerate(starting_numbers):
        seen_numbers[s] = [i + 1]

    staring_turn = len(starting_numbers) + 1
    spoken_number = starting_numbers[-1]
    for turn in trange(staring_turn, target_turn + 1):
        next_number = get_spoken_number(seen_numbers, spoken_number, turn)

        if next_number not in seen_numbers.keys():
            seen_numbers[next_number] = [turn]
        else:
            previous_indexes = seen_numbers[next_number]
            new_indexes = [max(previous_indexes), turn]
            seen_numbers[next_number] = new_indexes

        spoken_number = next_number

    print(next_number)


if __name__ == '__main__':
    main()
