def result() -> int:
    with open("./Day6/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    lines.append("")  # for last element distinction

    combined_group_responses = []
    row = ""
    for line in lines:
        if line == "":
            combined_group_responses.append(row)
            row = ""
        else:
            row += line

    group_response_count = []

    for gr in combined_group_responses:
        gr_set = set(gr)
        group_response_count.append(len(gr_set))

    group_all_yes_responses = []
    group = []
    for line in lines:
        if line == "":
            group_all_yes_responses.append(group)
            group = []
        else:
            group.append(line)

    group_yes_count = []
    for group_resp in group_all_yes_responses:
        intersection = set(group_resp.pop())
        for single_resp in group_resp:
            intersection = intersection.intersection(set(single_resp))

        yes_count = len(intersection)

        # yes_count = 0
        # for cgr in combined_group_responses:
        #     for c in set(cgr):
        #         yes_no = True
        #         for single_resp in group_resp:
        #             if c in single_resp:
        #                 continue
        #             else:
        #                 yes_no = False
        #                 break
        #         if yes_no:
        #             yes_count += 1

        group_yes_count.append(yes_count)

    return (sum(group_response_count), sum(group_yes_count))


r = result()