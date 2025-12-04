from itertools import product

maze = [list(line) for line in open("d4.in").read().splitlines()]

vecs = set(product(range(-1, 2), range(-1, 2)))
vecs.remove((0,0))

inbounds = lambda r, c: 0 <= r < len(maze) and 0 <= c < len(maze[0]) 
nbrs = lambda r,c: [(r+v1, c+v2) for v1, v2 in vecs if inbounds(r+v1, c+v2)]
val = lambda r,c: maze[r][c] == "@" if inbounds(r,c) else False
vals = lambda r,c: [val(r+v1,c+v2) for v1,v2 in vecs]

pos_to_cnt = dict()
for row, col in product(range(len(maze)), range(len(maze[0]))):
    pos_to_cnt[(row, col)] = float("inf")
    if maze[row][col] == "@":
        pos_to_cnt[(row,col)] = sum(vals(row, col))


# p1
print(sum(val < 4 for val in pos_to_cnt.values()))

removed = 1
tr = 0
while removed:
    removed = 0
    for (row, col), total in pos_to_cnt.items():
        if maze[row][col] == "@" and total < 4:
            maze[row][col] = "."
            removed += 1
            for nr, nc in nbrs(row, col):
                pos_to_cnt[(nr, nc)] -= 1
    tr += removed

# p2
print(tr)

