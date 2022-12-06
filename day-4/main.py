"""
This module solves the two challenges from Advent of Code 2022, day 4.
For challenge explanations, see https://adventofcode.com/2022/day/4

"""

def reformat(data):
    """
    Restructure input data, for use in answers
    1 and 2.
    """
    # Remove trailing blank line and split lines.
    data = data.strip().split("\n")

    # For each line, split elves into separate lists.
    data = [pair.split(",") for pair in data]

    # For each elf, transform intuitively written range
    # into set containing all numbers in the range.
    for p, pair in enumerate(data):
        for e, elf in enumerate(pair):
            start, end = elf.split("-")
            start, end = int(start), int(end) + 1
            if start == end:
                data[p][e] = set([start])
            else:    
                data[p][e] = set(list(range(start, end)))
    return data



def solve_c1(data):
    """
    Solve challenge 1.
    See https://adventofcode.com/2022/day/4
    """
    res = 0
    for pair in data:
        elf_1, elf_2 = pair[0], pair[1]
        common = elf_1.intersection(elf_2)
        if (common == elf_1) | (common == elf_2):
            res += 1
    return res



def solve_c2(data):
    """
    Solve challenge 2.
    See https://adventofcode.com/2022/day/4
    """
    res = 0
    for pair in data:
        elf_1, elf_2 = pair[0], pair[1]
        if len(elf_1.intersection(elf_2)):
            res += 1
    return res





if __name__ == "__main__":
    with open("day-4/input.txt", encoding="utf-8") as input_file:
        data = input_file.read()
    data = reformat(data)
    print(f"Solution to challenge 1 is: {solve_c1(data)}")
    print(f"Solution to challenge 2 is: {solve_c2(data)}")
