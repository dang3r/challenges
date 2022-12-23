import os
import math

lines = [line.split(" ") for line in open("09.in").read().splitlines()]
lines = [(line[0], int(line[1])) for line in lines]

dir_to_vec = {"R": (1, 0), "U": (0, 1), "D": (0, -1), "L": (-1, 0)}
touching = lambda p1, p2: abs(p1[0] - p2[0]) <= 1 and abs(p1[1] - p2[1]) <= 1


def vector_diff(dst, src):
    xdiff = dst[0] - src[0]
    ydiff = dst[1] - src[1]

    if xdiff == 0:
        return 0, int(ydiff / abs(ydiff))
    elif ydiff == 0:
        return int(xdiff / abs(xdiff)), 0
    return 1 if xdiff > 0 else -1, 1 if ydiff > 0 else -1


hpos = tpos = s = (0, 0)
tail_positions = set([tpos])
for dir, amt in lines:
    vec = dir_to_vec[dir]
    for i in range(amt):
        new_hpos = (hpos[0] + vec[0], hpos[1] + vec[1])
        if not touching(new_hpos, tpos):
            tpos = hpos
            tail_positions.add(tpos)
        hpos = new_hpos
print(len(tail_positions))


positions = [(0, 0) for _ in range(10)]
tail_positions = set([(0, 0)])
for dir, amt in lines:
    vec = dir_to_vec[dir]
    for i in range(amt):
        positions[0] = (positions[0][0] + vec[0], positions[0][1] + vec[1])
        for j in range(1, len(positions)):
            if touching(positions[j - 1], positions[j]):
                break
            elif not touching(positions[j - 1], positions[j]):
                diff = vector_diff(positions[j - 1], positions[j])
                positions[j] = (positions[j][0] + diff[0], positions[j][1] + diff[1])
        tail_positions.add(positions[-1])
print(len(tail_positions))
