"""
This module solves the two challenges from Advent of Code 2022, day 5.
For challenge explanations, see https://adventofcode.com/2022/day/5

"""

import re
import copy


def reformat(data):
    """
    Split stacks data and instructions.  Transform stacks to dictionary.
    """
    stacks0 = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    instructions0 = []
    for line in data.split("\n"):
        crates = re.findall(r"\[\D\]", line)
        if crates:
            stack_names = [m.start(0)//4 + 1 for m in re.finditer(r"\[\D\]", line)]
            for i, stack_name in enumerate(stack_names):
                stacks0[stack_name].append(crates[i])
        elif (line != "") & (bool(re.search("move", line))):
            instructions0.append(line.split()[1::2])
    return stacks0, instructions0



def solve_c1(stacks1, instructions1):
    """
    Solve challenge 1.
    See https://adventofcode.com/2022/day/5
    """
    res = ""

    for instruction in instructions1:
        num_crates = int(instruction[0])
        from_stack = int(instruction[1])
        to_stack = int(instruction[2])
        for crate in range(num_crates):
            stacks1[to_stack].insert(0, stacks1[from_stack].pop(0))

    for crate in stacks1.values():
        res = res + crate[0][1]

    assert res == "ZSQVCCJLL"
    return res



def solve_c2(stacks2, instructions2):
    """
    Solve challenge 2.
    See https://adventofcode.com/2022/day/5
    """
    assert type(stacks2) == dict
    res = ""

    for instruction in instructions2:
        num_crates = int(instruction[0])
        from_stack = int(instruction[1])
        to_stack = int(instruction[2])

        move = stacks2[from_stack][:num_crates]
        stacks2[from_stack] = stacks2[from_stack][num_crates:]
        stacks2[to_stack] = move + stacks2[to_stack]


    for crate in stacks2.values():
        res = res + crate[0][1]

    assert res == "QZFJRWHGS"
    return res





if __name__ == "__main__":
    with open("day-5/input.txt", encoding="utf-8") as input_file:
        data = input_file.read()
    stacks, instructions = reformat(data)
    print(f"Solution to challenge 1 is: {solve_c1(copy.deepcopy(stacks), instructions.copy())}")
    print(f"Solution to challenge 2 is: {solve_c2(copy.deepcopy(stacks), instructions.copy())}")
