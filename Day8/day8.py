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
    attempted_swaps = []
    ex_inst = []  # list of executed instructions
    accumulator = 0

    current_op_idx = 0

    while current_op_idx not in ex_inst:
        op = instructions[current_op_idx]
        if "acc" in op:
            op_split = op.split(" ")
            accumulator += int(op_split[1])
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
    return accumulator, ex_inst[-1]


r = result()

pass
