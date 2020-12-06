import math


def arithmetic_sum(first: int, delta: int, index: int):
    n = index + 1
    return int((n / 2) * (2 * first + (n - 1) * delta))


def compute_row(row: str) -> int:
    higher = 127
    lower = 0
    for idx in range(len(row)):
        if row[idx] == "F":  # front lower numbers
            h_delta = math.ceil((higher - lower) / 2)
            if h_delta == 1:
                return lower
            higher = higher - h_delta
        if row[idx] == "B":  # back higher numbers
            l_delta = math.ceil((higher - lower) / 2)
            if l_delta == 1:
                return higher
            lower = lower + l_delta


def compute_column(col: str) -> int:
    higher = 7
    lower = 0
    for idx in range(len(col)):
        if col[idx] == "L":
            h_delta = math.ceil((higher - lower) / 2)
            if h_delta == 1:
                return lower
            higher = higher - h_delta
        if col[idx] == "R":
            l_delta = math.ceil((higher - lower) / 2)
            if l_delta == 1:
                return higher
            lower = lower + l_delta


def compute_id(row: int, col: int) -> int:
    return row * 8 + col


def result() -> int:
    with open("./Day5/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    boarding_ids = []
    for line in lines:
        row = compute_row(line[:7])
        col = compute_column(line[7:])
        bpid = compute_id(row, col)
        boarding_ids.append(bpid)

    ascending_bids = sorted(boarding_ids)

    lower_val = ascending_bids[0]
    higher_val = ascending_bids[-1]

    accum = 0
    for i, seat in enumerate(ascending_bids):
        accum += seat
        expected_sum = arithmetic_sum(lower_val, 1, i)
        if not (accum == expected_sum):
            return seat - 1


r = result()
print(r)