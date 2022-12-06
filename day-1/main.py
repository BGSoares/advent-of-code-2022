"""
This module solves the two challenges from Advent of Code 2022, day 1.
For challenge explanations, see https://adventofcode.com/2022/day/1
"""



def reformat(data):
    data = data.split("\n\n")[:-1]
    data = [map(int, d.split("\n")) for d in data]
    data = [sum(elf) for elf in data]
    return data



def solve_c1(data):
    return max(data)



def solve_c2(data):
    return sum(sorted(data)[-3:])





if __name__ == "__main__":
    with open("day-1/input.txt", encoding="utf-8") as input_file:
        data = input_file.read()
    data = reformat(data)
    print(f"Solution to challenge 1 is: {solve_c1(data)}")
    print(f"Solution to challenge 2 is: {solve_c2(data)}")
