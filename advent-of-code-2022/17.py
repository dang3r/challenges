gusts = open("17.in").read().strip()

shapes = [
    ["####"],
    [
        ".#.",
        "###",
        ".#.",
    ],
    [
        "..#",
        "..#",
        "###",
    ],
    [
        "#",
        "#",
        "#",
        "#",
    ],
    [
        "##",
        "##",
    ],
]
grid = set([(col_idx, 0) for col_idx in range(7)])
gust_idx = 0
initial_width = 2
max_heights = [0 for _ in range(7)]


def intersect(shape, width, height):
    for y, row in enumerate(shape[::-1]):
        for x, col in enumerate(row):
            if col == "#":
                if width + x < 0 or width + x >= 7 or (width + x, height + y) in grid:
                    return True
    return False


def points(shape, width, height):
    for y, row in enumerate(shape[::-1]):
        for x, col in enumerate(row):
            if col == "#":
                yield width + x, height + y


def add_to_grid(shape, width, height):
    for x, y in points(shape, width, height):
        grid.add((x, y))


for rock_idx in range(2022):
    height = max(max_heights) + 4
    shape = shapes[rock_idx % len(shapes)]
    width = initial_width

    while True:
        new_width = width + 1 if gusts[gust_idx] == ">" else width - 1
        gust_idx = (gust_idx + 1) % len(gusts)

        # If shifting doesn't hit another shape or the walls, shift
        if not intersect(shape, new_width, height):
            width = new_width

        # If moving down hits another shape or wall, stop
        new_height = height - 1
        if intersect(shape, width, new_height):
            break
        height = new_height

    # Add all positions to grid
    add_to_grid(shape, width, height)
    for x, y in points(shape, width, height):
        max_heights[x] = max(max_heights[x], y)

print(max(max_heights))
