def result() -> int:
    with open("input_day_1.txt", "rt") as file:
        lines = file.readlines()

        entries = [int(l.strip()) for l in lines]

        return sum_and_compare_three(entries, 2020)


def sum_and_compare_three(entries: list, compareTo: int) -> int:
    for idx1, val1 in enumerate(entries):
        for idx2, val2 in enumerate(entries):
            for idx3, val3 in enumerate(entries):
                if idx1 != idx2 != idx3:
                    if val1 + val2 + val3 == compareTo:
                        return val1 * val2 * val3
