from q4.shared import read_passport_data
import re

count_fields = 8


def validate_byr(byr_txt):
    return 1920 <= int(byr_txt) <= 2002


def validate_iyr(iyr_txt):
    return 2010 <= int(iyr_txt) <= 2020


def validate_eyr(eyr_txt):
    return 2020 <= int(eyr_txt) <= 2030


def validate_height(hgt_txt):
    if 'cm' in hgt_txt:
        txt = 'cm'
        min_val = 150
        max_val = 193
    elif 'in' in hgt_txt:
        txt = 'in'
        min_val = 59
        max_val = 76
    else:
        raise ValueError('Invalid height field value')
    height = int(hgt_txt.replace(txt, ''))
    return min_val <= height <= max_val


def validate_hcl(hcl_txt):
    return re.match(r'(#[0-9a-f]{6})', hcl_txt)


def validate_ecl(ecl_txt):
    return ecl_txt in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(pid_txt):
    return re.match(r'(^[0-9]{9}$)', pid_txt)


def is_valid_passport(passport):
    if not validate_byr(passport['byr']):
        return False

    if not validate_iyr(passport['iyr']):
        return False

    if not validate_eyr(passport['eyr']):
        return False

    if not validate_height(passport['hgt']):
        return False

    if not validate_hcl(passport['hcl']):
        return False

    if not validate_ecl(passport['ecl']):
        return False

    if not validate_pid(passport['pid']):
        return False

    return True


def main():
    valid_passports = 0
    passports = read_passport_data()
    for p in passports:
        try:
            if is_valid_passport(p):
                valid_passports += 1
        except (ValueError, KeyError):
            pass
    print(valid_passports)


if __name__ == '__main__':
    assert validate_hcl('#123abc')
    assert not validate_hcl('#123abz')
    assert not validate_hcl('123abz')

    assert validate_ecl('brn')
    assert not validate_ecl('wat')

    assert validate_pid('000000001')
    assert not validate_pid('0123456789')
    main()
