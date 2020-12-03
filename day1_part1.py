def result() -> int:
    with open("input_day_1.txt", "rt") as file:
        lines = file.readlines()

        entries = [int(l.strip()) for l in lines]

        return sum_and_compare(entries, 2020)


def sum_and_compare(entries: list, compareTo: int) -> int:
    entries_copy = entries[:]

    indices = list(range(len(entries)))

    for index in indices:
        first_entry = entries_copy.pop(index)

        for second_entry in entries_copy:
            if first_entry + second_entry == compareTo:
                return first_entry * second_entry

        entries_copy = entries[:]