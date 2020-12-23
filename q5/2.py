from q5.shared import get_seat_id, read_passports


def main():
    passports = read_passports()
    seat_ids = [get_seat_id(p) for p in passports]

    my_seat = -1
    for seat_id in seat_ids:
        if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
            my_seat = seat_id + 1
            break
    print(my_seat)

if __name__ == '__main__':
    main()
