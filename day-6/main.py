"""
This module solves the two challenges from Advent of Code 2022, day 6.
For challenge explanations, see https://adventofcode.com/2022/day/6

"""

def reformat(data):
    """
    Remove white space from ends of data.
    """
    data = data.strip()
    return data



def solve_c(data, length):
    """
    Solve challenges 1 and 2.  Both challenges
    use the same logic, but require different
    values for the argument length.
    See https://adventofcode.com/2022/day/6
    """
    start = length
    end = len(data)
    for i in range(start, end):
        four_characters = data[i-length:i]
        if len(set(four_characters)) == length:
            return i





if __name__ == "__main__":
    with open("day-6/input.txt", encoding = "utf-8") as input_file:
        data = input_file.read()
    data = reformat(data)
    print(f"Solution for challenge 1 is: {solve_c(data, 4)}")
    print(f"Solution for challenge 2 is: {solve_c(data, 14)}")
