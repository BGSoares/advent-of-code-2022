"""
This module solves the two challenges from Advent of Code 2022, day 5.
For challenge explanations, see https://adventofcode.com/2022/day/5

"""

import re

def reformat(data):
    """
    Split stacks data and instructions.  Transform stacks to dictionary.
    """
    STACKS = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    INSTRUCTIONS = []
    for line in data.split("\n"):
        crates = re.findall(r"\[\D\]", line)
        if crates:
            stacks = [m.start(0)//4 + 1 for m in re.finditer(r"\[\D\]", line)]
            for i, stack in enumerate(stacks):
                STACKS[stack].append(crates[i])
        elif (line != "") & (bool(re.search("move", line))):
            INSTRUCTIONS.append(line.split()[1::2])
    return STACKS, INSTRUCTIONS


def solve_c1(stacks, instructions):
    """
    Solve challenge 1.
    See https://adventofcode.com/2022/day/5
    """
    stacks1 = stacks.copy()
    res = ""

    for instruction in instructions:
        num_crates = int(instruction[0])
        from_stack = int(instruction[1])
        to_stack = int(instruction[2])
        for crate in range(num_crates):
            stacks1[to_stack].insert(0, stacks1[from_stack].pop(0))

    for crate in stacks1.values():
        res = res + crate[0][1]
    return res


def solve_c2(stacks, instructions):
    """
    Solve challenge 2.
    See https://adventofcode.com/2022/day/5
    """
    stacks1 = stacks.copy()
    assert type(stacks1) == dict
    res = ""

    for instruction in instructions:
        num_crates = int(instruction[0])
        from_stack = int(instruction[1])
        to_stack = int(instruction[2])

        move = stacks1[from_stack][:num_crates]
        stacks1[from_stack] = stacks1[from_stack][num_crates:]
        stacks1[to_stack] = move + stacks1[to_stack]


    for crate in stacks1.values():
        res = res + crate[0][1]
    return res


if __name__ == "__main__":
    with open("day-5/input.txt", encoding="utf-8") as input_file:
        data = input_file.read()
    STACKS, INSTRUCTIONS = reformat(data)
    print(f"Solution to challenge 1 is: {solve_c1(STACKS, INSTRUCTIONS)}")
    STACKS, INSTRUCTIONS = reformat(data)
    print(f"Solution to challenge 2 is: {solve_c2(STACKS, INSTRUCTIONS)}")
