def op_swap(instructions: list, swap_op: tuple) -> list:
    inst_copy = instructions[:]
    # swap_op = (1,"jmp +24")
    idx = swap_op[0]
    op = swap_op[1]
    if "jmp" in op:
        op = op.replace("jmp", "nop")
    elif "nop" in op:
        op = op.replace("nop", "jmp")
    inst_copy[idx] = op

    return inst_copy


def find_op(instructions: list, swap_op: tuple) -> tuple:
    swapped_inst = op_swap(instructions, swap_op)
    max_idx = len(swapped_inst)
    ex_inst = []
    accum = 0
    current_op_idx = 0
    while current_op_idx not in ex_inst:
        if current_op_idx >= max_idx:
            return True, accum
        op = swapped_inst[current_op_idx]
        if "acc" in op:
            op_split = op.split(" ")
            accum += int(op_split[1])
            ex_inst.append(current_op_idx)
            current_op_idx += 1
        elif "jmp" in op:
            op_split = op.split(" ")
            jump_idx = int(op_split[1])
            ex_inst.append(current_op_idx)
            current_op_idx += jump_idx
        elif "nop" in op:
            # do nothing and continue, nop is still an instruction tho
            current_op_idx += 1
    return False, 0


def result() -> int:
    with open("./Day8/input.txt") as f:
        instructions = [line.strip() for line in f.readlines()]
    # instructions will have a list of op codes, acc, jmp and nop, can attempt to swap out either jmp for nop
    # or vice versa until program terminates, the program terminates if you can "escape" the instruction set
    # there are 597 (including 0) instructions you need to get an index that reaches >597
    # any jump that is negative and takes your index beyond 0 (into negative territory is probably not a good candidate)
    # have to walk it "backwards" meaning if index 344 causes inf loop then swap it with either nop or jmp (make note of the swap)
    # and continue until either idx is greater than 597 or found another inf loop, if so revert and swap that one out
    max_idx = len(instructions)
    potential_swaps = []

    for i, oper in enumerate(instructions):
        if "jmp" in oper:
            potential_swaps.append((i, oper))
        if "nop" in oper:
            potential_swaps.append((i, oper))

    for attempt in potential_swaps:
        result = find_op(instructions[:], attempt)
        if result[0]:
            return result[1]


r = result()

pass
