"""
This module solves the two challenges from Advent of Code 2022, day 2.
For challenge explanations, see https://adventofcode.com/2022/day/2
"""



RULES = {"A": [1,"C","B"], "B": [2,"A","C"], "C": [3,"B","A"]}


def reformat(data):
    data = data.split("\n")[:-1]
    data = [line.split(" ") for line in data]
    return data



def solve_c1(data):
    CONVERT = {"X":"A", "Y":"B", "Z":"C"}

    result = []
    for game in data:
        elf = game[0]
        you = CONVERT[game[1]]
        base_points = RULES[you][0]
        if elf == you:
            result.append(3 + base_points)
        elif elf == RULES[you][1]:
            result.append(6 + base_points)
        else:
            result.append(base_points)
    return sum(result)



def solve_c2(data):

    result = []
    for game in data:
        elf = game[0]
        strategy = game[1]

        if strategy == "X":
            you = RULES[elf][1]
            result.append(0 + RULES[you][0])
        elif strategy == "Y":
            result.append(3 + RULES[elf][0])
        else:
            you = RULES[elf][2]
            result.append(6 + RULES[you][0])
    return sum(result)





if __name__ == "__main__":
    with open("day-2/input.txt", encoding = "utf-8") as input_file:
        data = input_file.read()
    data = reformat(data)
    print(f"Solution to challenge 1 is: {solve_c1(data)}")
    print(f"Solution to challenge 2 is: {solve_c2(data)}")
