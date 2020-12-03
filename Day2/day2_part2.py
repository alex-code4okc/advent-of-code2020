def result() -> int:
    result = None
    with open("input_day2.txt", "rt") as file:
        lines = file.readlines()
        # remove new lines
        lines = [l.strip() for l in lines]

        acceptable = []

        for line in lines:
            condition, password = line.split(":")
            min_max, character = condition.split(" ")
            pos1, pos2 = min_max.split("-")

            pos1 = int(pos1) - 1
            pos2 = int(pos2) - 1
            password = password.strip()

            condition1 = password[pos1] == character
            condition2 = password[pos2] == character
            if (condition1 and not condition2) or (not condition1 and condition2):
                acceptable.append(True)
            else:
                acceptable.append(False)

        result = acceptable.count(True)
    return result


result()