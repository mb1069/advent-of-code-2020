from q2.shared import read_db, unpack_policy


def is_valid_password(first_index, sec_index, policy_char, password):
    chars = [password[i-1] for i in [first_index, sec_index]]
    return sum([c == policy_char for c in chars]) == 1


def main():
    valid_passwords = 0
    for l in read_db():
        policy_case = unpack_policy(l)
        if is_valid_password(*policy_case):
            valid_passwords += 1
    print(valid_passwords)


if __name__ == '__main__':
    main()
