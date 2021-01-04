from q13.shared import read_file
import math


def filter_inactive_buses(schedules):
    return [int(s) for s in schedules if s != 'x']


def find_earliest_bus(early_start, schedules):
    best_bus = None
    wait_time = 1000000
    for s in schedules:
        if early_start // s == 0:
            best_bus = s
            wait_time = 0
            break
        else:
            # If not a multiple of start time
            departure_time = math.ceil(early_start / s) * s
            s_wait_time = departure_time - early_start
            if s_wait_time < wait_time:
                wait_time = s_wait_time
                best_bus = s
    return best_bus, wait_time


def main():
    early_start, schedules = read_file()
    schedules = filter_inactive_buses(schedules)

    best_bus, wait_time = find_earliest_bus(early_start, schedules)
    print('Best bus: ', best_bus)
    print('Wait time: ', wait_time)
    print(best_bus * wait_time)


if __name__ == '__main__':
    main()
