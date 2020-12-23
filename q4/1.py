from q4.shared import read_passport_data

count_fields = 8


def is_valid_passport(passport):
    field_names = list(passport.keys())
    if 'cid' not in field_names:
        return len(field_names) == count_fields - 1

    return len(field_names) == count_fields


def main():
    valid_passports = 0
    passports = read_passport_data()
    for p in passports:
        if is_valid_passport(p):
            valid_passports += 1
    print(valid_passports)


if __name__ == '__main__':
    main()
