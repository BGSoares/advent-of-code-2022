"""
This module solves the two challenges from Advent of Code 2022, day 3.
For challenge explanations, see https://adventofcode.com/2022/day/3
"""

def reformat(data):
    data = data.split("\n")
    return data



def get_priority(item):
    priority = ord(item)
    if (priority >= 97) & (priority <= 122):
        return int(priority - 96)
    if (priority >= 65) & (priority <= 90):
        return int(priority - 38)



def solve_c1(data):
    score = 0
    for rucksack in data:
        item_count = len(rucksack)
        pocket_1 = rucksack[:item_count//2]
        pocket_2 = rucksack[item_count//2:]
        assert(len(pocket_1)==len(pocket_2))

        common = set(pocket_1).intersection(set(pocket_2))
        common = list(common)[0]

        score += get_priority(common)
    return score



def solve_c2(data):
    score = 0
    for _ in range(len(data)//3):
        elf1 = set(data.pop())
        elf2 = set(data.pop())
        elf3 = set(data.pop())

        common = elf1.intersection(elf2).intersection(elf3)
        common = list(common)[0]
        priority = get_priority(common)

        score += priority
    return score





if __name__ == "__main__":
    with open("day-3/input.txt") as input:
        data = input.read()[:-1]
    data = reformat(data)
    print(f"Solution to challenge 1 is: {solve_c1(data)}")
    print(f"Solution to challenge 2 is: {solve_c2(data)}")
