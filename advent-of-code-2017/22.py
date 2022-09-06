
lines = [line.strip() for line in open("22.in").readlines()]
grid = dict()
total_infected = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        grid[f"{j}_{i}"] = char
        if char == "#":
            total_infected += 1
pos = (len(lines[0]) // 2, len(lines) // 2)

right = {
    (0,-1):(1,0),
    (1,0):(0,1),
    (0,1):(-1,0),
    (-1,0):(0, -1)
}
left = {v:k for k, v in right.items()}

def coord():
    return f"{pos[0]}_{pos[1]}"

def element():
    c = coord()
    return grid.get(c, ".")

def part1():
    global vector, pos
    vector = (0, -1)
    infections = 0
    for i in range(10000):
        if element() == "#":
            grid[coord()] = "."
            vector = right[vector]
        else:
            infections += 1
            grid[coord()] = "#"
            vector = left[vector]
        pos = (pos[0]+ vector[0], pos[1] + vector[1])
    print(infections)

def part2():
    global vector, pos
    infections = 0
    for _ in range(10000000):
        el = element()
        if el == ".":
            vector = left[vector]
            grid[coord()] = "W"
        elif el == "W":
            infections += 1
            grid[coord()] = "#"
        elif el == "#":
            vector = right[vector]
            grid[coord()] = "F"
        elif el == "F":
            vector = (vector[0] * -1, vector[1] * -1)
            grid[coord()] = "."
        pos = (pos[0]+ vector[0], pos[1] + vector[1])
    print(infections)

part1()
#reset
lines = [line.strip() for line in open("22.in").readlines()]
grid = dict()
total_infected = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        grid[f"{j}_{i}"] = char
pos = (len(lines[0]) // 2, len(lines) // 2)
vector = (0, -1)
part2()