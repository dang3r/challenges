import re

games = open("d2.in").read().splitlines()
maxes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# part 2
total = 0
for idx, game in enumerate(games):
    good = True
    for num, colour in re.findall("(\d+) (red|blue|green)", game):
        if int(num) > maxes[colour]:
            good = False
            break
    if good:
        total += idx + 1
print(total)

# part 2
total = 0
for idx, game in enumerate(games):
    good = True
    mins = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for num, colour in re.findall("(\d+) (red|blue|green)", game):
        mins[colour] = max(mins[colour], int(num))
    power = mins["red"] * mins["blue"] * mins["green"]
    total += power
print(total)
