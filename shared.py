def read_txt_single_col_nums(txtfile: str, dtype: object):
    with open(txtfile) as f:
        raw_lines = f.readlines()
    numbers = [dtype(l.strip()) for l in raw_lines]

    return numbers
