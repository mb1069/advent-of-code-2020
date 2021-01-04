from q13.shared import read_file
import math
import numpy as np

from fractions import Fraction, gcd
from functools import reduce
from scipy.optimize import fsolve


def filter_inactive_buses(_schedules):
    schedules = []
    offsets = []
    for i, s in enumerate(_schedules):
        if s != 'x':
            schedules.append(int(s))
            offsets.append(i)

    return schedules, offsets


def timetable(schedules, offsets):
    print('\t'.join(['time'] + [str(s) for s in schedules]))
    for t in range(1068780, 1068780 + 10):
        starts = ['D' if (t) % s == 0 else '.' for s, o in zip(schedules, offsets)]
        print('\t'.join([str(t)] + starts))


# Chinese remainder theorem
def get_ratios(schedules, offsets):
    multi = schedules.pop(0)
    _ = offsets.pop(0)
    time = multi
    while len(schedules):
        next_multi = schedules.pop(0)
        next_offset = offsets.pop(0)

        while (time + next_offset) % next_multi != 0:
            time += multi
        multi = multi * next_multi
        print(next_multi, time, next_multi % time)
    return time


# Naive solution, working but not tractable for large problem
def get_ratios_naive(schedules, offsets):
    m = 0
    solved = False
    time = schedules[0]
    while not solved:
        time = schedules[0] * m
        print(time)
        solved = True
        for s, o in zip(schedules[1:], offsets[1:]):
            print(s, s // (time + o))
            if (time + o) % s != 0:
                m += 1
                print('Break')
                solved = False
                break
            print('OK')
    print(time)


def main():
    early_start, schedules = read_file()
    schedules, offsets = filter_inactive_buses(schedules)
    # timetable(schedules, offsets)
    get_ratios(schedules, offsets)
    # print('Best bus: ', best_bus)
    # print('Wait time: ', wait_time)
    # print(best_bus * wait_time)


if __name__ == '__main__':
    main()
