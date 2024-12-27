import os

data = [[int(val) for val in line.strip()] for line in open("d10.in").readlines()]
MAX_X = len(data[0])
MAX_Y = len(data)


def trailhead_score(x: int, y: int):
    val = data[y][x]
    next_val = val + 1
    if val == 9:
        return set([(x, y)]), 1

    candidates = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
    t_total = set()
    t_rating = 0
    for cx, cy in candidates:
        if 0 <= cx < MAX_X and 0 <= cy < MAX_Y and data[cy][cx] == next_val:
            score, rating = trailhead_score(cx, cy)
            t_total.update(score)
            t_rating += rating

    return t_total, t_rating


t_total = 0
t_rating = 0
for x in range(MAX_X):
    for y in range(MAX_Y):
        if data[y][x] == 0:
            score, rating = trailhead_score(x, y)
            t_total += len(score)
            t_rating += rating
print(t_total)
print(t_rating)
