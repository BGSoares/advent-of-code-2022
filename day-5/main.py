
import re

def reformat(data):
    STACKS = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    INSTRUCTIONS = []
    data = data.split("\n")
    for line in data:
        crates = re.findall(r"\[\D\]", line)
        if crates:
            stacks = [m.start(0)//4 + 1 for m in re.finditer(r"\[\D\]", line)]
            for i, stack in enumerate(stacks):
                STACKS[stack].append(crates[i])
        elif (line != "") & (bool(re.search("move", line))):
            INSTRUCTIONS.append(line.split()[1::2])
    return STACKS, INSTRUCTIONS


def solve_c1(STACKS, INSTRUCTIONS):
    res = ""
    for instruction in INSTRUCTIONS:
        # print("instruction: ", instruction)
        num_crates = int(instruction[0])
        from_stack = int(instruction[1])
        to_stack = int(instruction[2])
        # print("from_stack: ", STACKS[from_stack])
        # print("to_stack: ", STACKS[to_stack])

        move = STACKS[from_stack][:num_crates]
        # print("move: ", move)
        STACKS[to_stack] = move + STACKS[to_stack]
        # print("to_stack after", STACKS[to_stack])
        STACKS[from_stack] = STACKS[from_stack][num_crates:]
        # print("from_stack after", STACKS[from_stack])

    
    for crate in STACKS.values():
        res = res + crate[0][1]
    return res


if __name__ == "__main__":
    with open("day-5/input.txt") as input:
        data = input.read()
    STACKS, INSTRUCTIONS = reformat(data)
    # print(INSTRUCTIONS)
    print(f"Solution to challenge 1 is: {solve_c1(STACKS, INSTRUCTIONS)}")
