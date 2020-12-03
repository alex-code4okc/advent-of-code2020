def result() -> int:
    with open("input_day2.txt", "rt") as file:
        lines = file.readlines()
        # remove new lines
        lines = [l.strip() for l in lines]

        acceptable = []

        for line in lines:
            condition, password = line.split(":")
            min_max, character = condition.split(" ")
            minimum, maximum = min_max.split("-")

            minimum = int(minimum)
            maximum = int(maximum)
            character_count = password.count(character)
            password = password.strip()
            if minimum <= character_count and character_count <= maximum:
                acceptable.append(True)
            else:
                acceptable.append(False)

        return acceptable.count(True)
