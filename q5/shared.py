import os
import math


def find_seat(row_txt, low_char, min_val=0, max_val=127):
    avg_row = int((max_val + min_val) / 2)
    if row_txt[0] == low_char:
        max_val = avg_row
    else:
        min_val = avg_row + 1

    if min_val == max_val:
        return min_val
    return find_seat(row_txt[1:], low_char, min_val, max_val)


def calc_seat_id(row, col):
    return (row * 8) + col


def get_seat_id(txt):
    txt = list(txt)
    row_txt = txt[0:7]
    col_txt = txt[7:]
    row = find_seat(row_txt, low_char='F', min_val=0, max_val=127)
    col = find_seat(col_txt, low_char='L', min_val=0, max_val=7)
    return calc_seat_id(row, col)


def read_passports():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        lines = f.readlines()
    return [l.strip() for l in lines]
