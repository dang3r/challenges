import sys
import functools

#sys.setrecursionlimit(15000)
lines = [list(line) for line in open("d7.in").readlines()]
#lines = [list(line) for line in open("d7.testin").readlines()]

cols = [lines[0].index("S")]

splits = 0
for line in lines[1:]:
    new_cols = []
    for col in cols:
        if line[col] == ".":
            line[col] = "|"
            new_cols.append(col)
        elif line[col] == "^":
            splits += 1
            for c in [col-1,col+1]:
                if 0 <= c < len(line):
                    line[c] == "|"
                    new_cols.append(c)
    cols = new_cols

print(splits)

@functools.lru_cache
def dfs(row, col):
    while row < len(lines) and lines[row][col] != "^":
        row += 1
    if row == len(lines):
        return 1
    return dfs(row, col-1) + dfs(row, col+1)

total = dfs(0, lines[0].index("S"))
print(total)





