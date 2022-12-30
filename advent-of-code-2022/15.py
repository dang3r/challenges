import re

lines = open("15.in").read().splitlines()
matches = [[int(val) for val in re.findall("-?\d+", line)] for line in lines]
row = 2000000

manhattan_distance = lambda x1, y1, x2, y2: abs(x2 - x1) + abs(y2 - y1)
min_x = float("inf")
max_x = float("-inf")
for sx, sy, bx, by in matches:
    dist = manhattan_distance(sx, sy, bx, by)
    min_x = min(min_x, sx, bx, sx - dist)
    max_x = max(max_x, sx, bx, sx + dist)


total_taken = 0
print(min_x, max_x)
for i in range(min_x, max_x + 1):
    pt = (i, row)
    if any(pt == (sx, sy) or (pt == (bx, by)) for sx, sy, bx, by in matches):
        continue
    for sx, sy, bx, by in matches:
        dist_short = manhattan_distance(sx, sy, bx, by)
        dist_to_pt = manhattan_distance(sx, sy, i, row)
        if dist_to_pt <= dist_short:
            total_taken += 1
            break
print(total_taken)

width = 4000000
for y in range(0, width + 1):
    if y % 100000 == 0:
        print(y)
    vals = []
    for sx, sy, bx, by in matches:
        dist = manhattan_distance(sx, sy, bx, by)
        h = dist * 2 + 1
        max_y = sy + dist
        min_y = sy - dist
        if min_y <= y <= max_y:
            delta_y = abs(y - sy)
            length = h - delta_y * 2
            x = sx - length // 2
            vals.append((x, length))
    vals = sorted(vals)
    done = False
    min_x = vals[0][0]
    max_x = vals[0][0] + vals[0][1] - 1
    for x, l in vals[1:]:
        if x == max_x + 2:
            print("DONE", (x - 1) * 4000000 + y)
            done = True
            break
        else:
            max_x = max(max_x, x + l - 1)
    if done:
        break
