from collections import defaultdict

lines = open("d3.in").read().splitlines()

star_to_numbers = defaultdict(set)


def neighbours(x, y):
    vecs = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]
    for x_vec, y_vec in vecs:
        coord = x + x_vec, y + y_vec
        if 0 <= coord[0] < len(lines[0]) and 0 <= coord[1] < len(lines):
            yield coord


def nearby_symbol(x, y):
    for c_x, c_y in neighbours(x, y):
        char = lines[c_y][c_x]
        if not char.isdigit() and char != ".":
            return True
    return False


def nearby_star(x, y):
    for c_x, c_y in neighbours(x, y):
        char = lines[c_y][c_x]
        if char == "*":
            yield c_x, c_y


total = 0
for y, line in enumerate(lines):
    x = 0
    while x < len(line):
        num_str = ""
        symbol_seen = False
        stars = set()
        while x < len(line) and line[x].isdigit():
            num_str += line[x]
            symbol_seen |= nearby_symbol(x, y)
            for star in nearby_star(x, y):
                stars.add(star)
            x += 1
        stars = set(stars)
        if num_str and symbol_seen:
            total += int(num_str)
        if num_str and stars:
            for star in stars:
                star_to_numbers[star].add((y, x - 1, int(num_str)))
        x += 1
print(total)


sum_gears = 0
for star, values in star_to_numbers.items():
    if len(values) == 2:
        values = list(values)
        sum_gears += values[0][2] * values[1][2]
print(sum_gears)
