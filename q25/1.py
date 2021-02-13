from q25.shared import read_file

subject_number = 7


def transform(subject_number, loop_size):
    l = 0
    val = 1
    while l < loop_size:
        val *= subject_number
        val %= 20201227
        l += 1
    return val


def find_loop_size(target_number):
    l = 0
    val = 1
    while True:
        val *= subject_number
        val %= 20201227
        l += 1
        if val == target_number:
            return l


def main():
    card_pkey, door_pkey = read_file()

    card_loopsize = find_loop_size(card_pkey)
    door_loopsize = find_loop_size(door_pkey)

    card_est_encrypt_key = transform(card_pkey, door_loopsize)
    door_est_encrypt_key = transform(door_pkey, card_loopsize)
    print(card_loopsize, door_loopsize)
    print(card_est_encrypt_key, door_est_encrypt_key)


if __name__ == '__main__':
    main()
