"""
This module solves the two challenges from Advent of Code 2022, day 8.
For challenge explanations, see https://adventofcode.com/2022/day/8
"""
import numpy as np

def parse(input_data):
    """
    Parse input input_data.
    """
    wip_data = input_data.strip().split("\n")
    wip_data = [[int(tree) for tree in line] for line in wip_data]
    res_data = np.array(wip_data, dtype=object)
    return res_data


def solve_c1(forest):
    """
    Solve challenges 2.
    See https://adventofcode.com/2022/day/8
    """
    res = 4 * (len(forest)-1)
    start = 1
    end = len(forest) - 1
    for row in range(start, end):
        for column in range(start, end):
            left = max(forest[row,:column])
            right = max(forest[row,column+1:])
            top = max(forest[:row,column])
            bottom = max(forest[row+1:,column])
            tree = forest[row,column]
            if (tree > left) | (tree > right) | (tree > top) | (tree > bottom):
                res += 1
    return res


def solve_c2(forest):
    """
    Solve challenges 2.
    See https://adventofcode.com/2022/day/8
    """
    res = 0
    start = 1
    end = len(forest) - 1
    for row in range(start, end):
        for column in range(start, end):
            tree = forest[row,column]

            left_trees = np.flip(forest[row,:column])
            left_tallest = max(left_trees)
            if tree > left_tallest:
                left = len(left_trees)
            else:
                left = np.argmax(left_trees >= tree) + 1

            right_trees = forest[row,column+1:]
            right_tallest = max(right_trees)
            if tree > right_tallest:
                right = len(right_trees)
            else:
                right = np.argmax(right_trees >= tree) + 1

            top_trees = np.flip(forest[:row,column])
            top_tallest = max(top_trees)
            if tree > top_tallest:
                top = len(top_trees)
            else:
                top = np.argmax(top_trees >= tree) + 1

            bottom_trees = forest[row+1:,column]
            bottom_tallest = max(bottom_trees)
            if tree > bottom_tallest:
                bottom = len(bottom_trees)
            else:
                bottom = np.argmax(bottom_trees >= tree) + 1

            score = left * right * top * bottom

            if score > res:
                res = score
    return res

if __name__ == "__main__":
    with open("day-8/input.txt", encoding="utf-8") as input_file:
        data = input_file.read()
    data = parse(data)
    print(f"Solution to challenge 1 is: {solve_c1(data)}")
    print(f"Solution to challenge 1 is: {solve_c2(data)}")
