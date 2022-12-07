
import re

def solve_c1(lines):
    lines = lines.strip().split("\n")

    dir_sizes = {}
    current_dir = ""

    for line in lines:
        if bool(re.search("\$ cd", line)):
            # print("line: ", line)
            _, _, dirname = line.split(" ")
            if dirname == "/":
                current_dir = "/"
            elif bool(re.match("^[a-z]*$", dirname)):
                current_dir = current_dir + "/" + dirname
            elif bool(re.search("..", dirname)):
                keep_until = re.search("(?s:.*)/", current_dir).end() - 1
                current_dir = current_dir[:keep_until]

        elif (line == "$ ls") | (bool(re.search("^dir ", line))):
            continue

        elif bool(re.match("[1-9]", line[0])):
            # print("line: ", line)
            size, _ = line.split(" ")
            if current_dir in dir_sizes:
                dir_sizes[current_dir] += int(size)
            else:
                dir_sizes[current_dir] = int(size)
            # print("dictionary value: ", dir_sizes[current_dir])

    res = 0
    for size in dir_sizes.values():
        if size <= 100000:
            res += size
    print(dir_sizes)
    return res

if __name__ == "__main__":
    with open("day-7/input.txt", encoding="utf-8") as input_file:
        data = input_file.read()
    print(f"Solution to challenge 1 is: {solve_c1(data)}")
