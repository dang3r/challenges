import re

commands = open("d6.in").read().splitlines()


def set_lights(d, rng1, rng2, change):
    for y in range(rng1[1], rng2[1] + 1):
        for x in range(rng1[0], rng2[0] + 1):
            d[y][x] = change(d[y][x])


d = [[0 for _ in range(1000)] for a in range(1000)]
d2 = [[0 for _ in range(1000)] for a in range(1000)]

for cmd in commands:
    vals = re.findall("(\d+,\d+)", cmd)
    assert len(vals) == 2
    rng1, rng2 = [tuple(map(int, val.split(","))) for val in vals]
    if "off" in cmd:
        set_lights(d, rng1, rng2, change=lambda x: 0)
        set_lights(d2, rng1, rng2, change=lambda x: max(x - 1, 0))
    elif "on" in cmd:
        set_lights(d, rng1, rng2, change=lambda x: 1)
        set_lights(d2, rng1, rng2, change=lambda x: x + 1)
    elif "toggle" in cmd:
        set_lights(d, rng1, rng2, change=lambda x: x ^ 1)
        set_lights(d2, rng1, rng2, change=lambda x: x + 2)


on = sum(sum(row) for row in d)
print(on)
on = sum(sum(row) for row in d2)
print(on)
