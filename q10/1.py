from q10.shared import read_file


def find_chain(nums):
    jolt = 0
    single_jolts = 0
    triple_jolts = 1
    while len(nums):
        adaptor = nums.pop(0)
        if jolt - adaptor <= 3:
            if adaptor - jolt == 1:
                single_jolts += 1
            elif adaptor - jolt == 3:
                triple_jolts += 1
            jolt = adaptor
        else:
            break
    return single_jolts * triple_jolts


def main():
    nums = sorted(read_file())
    max_jolt = find_chain(nums)
    print(max_jolt)


if __name__ == '__main__':
    main()
