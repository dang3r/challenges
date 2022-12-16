import math
import copy

lines = [line.rstrip("\n") for line in open("05.in").readlines()]
num_columns = math.ceil(len(lines[0]) / 4)
cols = [[] for _ in range(num_columns)]

for line_idx, line in enumerate(lines):
    if line[1] == "1":
        break
    for i, idx in enumerate(range(1, len(lines[0]), 4)):
        char = line[idx].strip()
        if char:
            cols[i].append(char)
for col in cols:
    col.reverse()


def part1(lines, cols):
    for line in lines:
        tokens = line.split(" ")
        num, src_col, dst_col = list(map(int, tokens[1::2]))
        for _ in range(num):
            cols[dst_col - 1].append(cols[src_col - 1].pop())
    print("".join(col[-1] for col in cols))


def part2(lines, cols):
    for line in lines:
        tokens = line.split(" ")
        num, src_col, dst_col = list(map(int, tokens[1::2]))
        src_col -= 1
        dst_col -= 1
        rm_idx = len(cols[src_col]) - num
        new_cols = cols[src_col][rm_idx:]
        cols[src_col] = cols[src_col][:rm_idx]
        cols[dst_col].extend(new_cols)
    print("".join(col[-1] for col in cols))


part1(lines[line_idx + 2 :], copy.deepcopy(cols))
part2(lines[line_idx + 2 :], copy.deepcopy(cols))
