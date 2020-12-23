from q5.shared import get_seat_id, read_passports


def main():
    max_seat_id = -1
    passports = read_passports()
    for p in passports:
        print(p)
        seat_id = get_seat_id(p)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    print(max_seat_id)


if __name__ == '__main__':
    main()
