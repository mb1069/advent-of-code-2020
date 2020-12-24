from q8.shared import read_file, HandHeldDevice


def main():
    instructions = read_file()

    dev = HandHeldDevice()
    final_state = dev.run(instructions)
    print(dev.accumulator)


if __name__ == '__main__':
    main()
