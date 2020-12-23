from q2.shared import read_db, unpack_policy


def is_valid_password(min_val, max_val, policy_char, password):
    count_policy_char = password.count(policy_char)
    return min_val <= count_policy_char <= max_val


def main():
    valid_passwords = 0
    for l in read_db():
        policy_case = unpack_policy(l)
        if is_valid_password(*policy_case):
            valid_passwords += 1
    print(valid_passwords)


if __name__ == '__main__':
    main()
