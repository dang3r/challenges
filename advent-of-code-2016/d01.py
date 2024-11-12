vectors = open("01.in").read().split(", ")

NORTH, SOUTH, EAST, WEST = range(4)
heading = NORTH
heading_to_vec = {NORTH: (0, 1), SOUTH: (1, 0), EAST: (0, -1), WEST: (-1, 0)}
x, y = 0, 0
seen = set([(x, y)])
home_found = False
next_heading = lambda d: (heading + (1 if d == "R" else -1)) % 4

for vector in vectors:
    steps = int(vector[1:])
    dir = vector[0]
    heading = next_heading(dir)
    vec = heading_to_vec[heading]

    if not home_found:
        for idx in range(1, steps + 1):
            new_x, new_y = x + idx * vec[0], y + idx * vec[1]
            if (new_x, new_y) in seen:
                print(f"P2 ({new_x}, {new_y})", abs(new_x) + abs(new_y))
                home_found = True
            seen.add((new_x, new_y))
    x, y = (x + steps * vec[0], y + steps * vec[1])

print("P1", abs(x) + abs(y))
