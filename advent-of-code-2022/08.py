lines = [list(map(int, line)) for line in open("08.in").read().splitlines()]
height = len(lines)
width = len(lines[0])
seen = set()

is_edge = lambda x, y: x == 0 or x == width - 1 or y == 0 or y == height - 1

for y in range(height):
    mx_left = -1
    mx_right = -1
    for x in range(width):
        # left
        if is_edge(x, y) or lines[y][x] > mx_left:
            mx_left = lines[y][x]
            seen.add((x, y))
        if is_edge(width - 1 - x, y) or lines[y][width - 1 - x] > mx_right:
            mx_right = lines[y][width - 1 - x]
            seen.add((width - 1 - x, y))

for x in range(width):
    my_up = -1
    my_down = -1
    for y in range(height):
        # left
        if is_edge(x, y) or lines[y][x] > my_up:
            my_up = lines[y][x]
            seen.add((x, y))
        if is_edge(x, height - 1 - y) or lines[height - 1 - y][x] > my_down:
            my_down = lines[height - 1 - y][x]
            seen.add((x, height - 1 - y))
print(len(seen))

max_sight = -1
for y in range(height):
    for x in range(width):
        tree_height = lines[y][x]
        product = 1
        distances = []
        for vec in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            pos = (y + vec[0], x + vec[1])
            distance = 1
            while (
                0 < pos[0] < height - 1
                and 0 < pos[1] < width - 1
                and lines[pos[0]][pos[1]] < tree_height
            ):
                distance += 1
                pos = (pos[0] + vec[0], pos[1] + vec[1])
            distances.append(distance)
            product *= distance
        print(y, x, product, distances)
        max_sight = max(max_sight, product)
print(max_sight)
