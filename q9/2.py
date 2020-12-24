from q9.shared import find_preamble_limit, read_file

preamble_length = 25


def find_contiguous_sum(target_sum):
    numbers = [int(n) for n in read_file()]
    start_index = 0
    end_index = 1
    current_sum = numbers[start_index] + numbers[end_index]

    while current_sum != target_sum:
        if current_sum < target_sum:
            end_index += 1
            current_sum += numbers[end_index]
        else:
            current_sum -= numbers[start_index]
            start_index += 1

    list_sum = numbers[start_index:end_index]
    print(f'Total: {min(list_sum) + max(list_sum)}')


def main():
    l = find_preamble_limit(preamble_length)
    find_contiguous_sum(l)


if __name__ == '__main__':
    main()
