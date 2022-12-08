
import numpy as np

def parse(data):
    data = data.strip().split("\n")
    data = [[int(tree) for tree in line] for line in data]
    data = np.array(data, dtype=object)
    return data


def solve_c1(data):
    res = 4 * (len(data)-1)
    start = 1
    end = len(data) - 1
    for r in range(start, end):
        for c in range(start, end):
            left = max(data[r,:c])
            right = max(data[r,c+1:])
            top = max(data[:r,c])
            bottom = max(data[r+1:,c])
            tree = data[r,c]
            if (tree > left) | (tree > right) | (tree > top) | (tree > bottom):
                res += 1
    return res


def solve_c2(data):
    res = 0
    start = 1
    end = len(data) - 1
    for row in range(start, end):
        for column in range(start, end):
            tree = data[row,column]

            left_trees = np.flip(data[row,:column])
            left = np.argmax(left_trees >= tree) + 1

            right_trees = data[row,column+1:]
            right = np.argmax(right_trees >= tree) + 1

            top_trees = np.flip(data[:row,column])
            top = np.argmax(top_trees >= tree) + 1

            bottom_trees = data[row+1:,column]
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
