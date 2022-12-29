from collections import defaultdict
import re

lines = open("14.in").read().splitlines()


def coords(lines):
    c = defaultdict(set)
    for line in lines:
        matches = [
            list(map(int, match.split(","))) for match in re.findall("\d+,\d+", line)
        ]
        for i, (x, y) in enumerate(matches):
            c[x].add(y)
            if i != 0:
                prev = tuple(matches[i - 1])
                diff = [x - matches[i - 1][0], y - matches[i - 1][1]]
                if diff[0] != 0:
                    diff[0] /= int(abs(diff[0]))
                else:
                    diff[1] /= int(abs(diff[1]))
                while prev != (x, y):
                    prev = prev[0] + diff[0], prev[1] + diff[1]
                    c[int(prev[0])].add(int(prev[1]))
    return c


def neighbour(x, y, coords, max_y=None):
    for vec in [(0, 1), (-1, 1), (1, 1)]:
        x_new = x + vec[0]
        y_new = y + vec[1]
        if max_y and y_new == max_y:
            print("hit max_y")
            return
        if (x_new not in coords) or (x_new in coords and y_new not in coords[x_new]):
            return x_new, y_new


def sand(start_x, start_y, coords):
    total = 0
    while True:
        x, y = start_x, start_y
        print("Starting")
        while neighbour(x, y, coords):
            x, y = neighbour(x, y, coords)
            print("neighbour", x, y)
            if x not in coords or (
                x in coords and not any(c_y >= y for c_y in coords[x])
            ):
                return total
        total += 1
        coords[x].add(y)


def sand_p2(start_x, start_y, coords):
    max_y = -1
    for x in coords:
        for y in coords[x]:
            max_y = max(max_y, y)
    max_y += 2
    total = 0
    while True:
        x, y = start_x, start_y
        while neighbour(x, y, coords, max_y=max_y):
            x, y = neighbour(x, y, coords, max_y=max_y)
        total += 1
        coords[x].add(y)
        if (x, y) == (start_x, start_y):
            return total


c = coords(lines)
print(c)
print(sand(500, 0, coords(lines)))
print(sand_p2(500, 0, coords(lines)))
