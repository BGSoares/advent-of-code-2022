"""
This module solves the two challenges from Advent of Code 2022, day 1.
For challenge explanations, see https://adventofcode.com/2022/day/1
"""

def reformat(data):
    data = data.split("\n\n")[:-1]
    data = [map(int, d.split("\n")) for d in data]
    data = [sum(elf) for elf in data]
    return data


def solve_p1(data):
    return max(data)


def solve_p2(data):
    return sum(sorted(data)[-3:])



if __name__ == "__main__":
    with open("day-1/input.txt") as input:
        data = input.read()
    data = reformat(data)
    print(f"Solution to problem 1 is: {solve_p1(data)}")
    print(f"Solution to problem 2 is: {solve_p2(data)}")
