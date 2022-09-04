from copy import deepcopy

state = [
    list(".#."),
    list("..#"),
    list("###")
]

def flip_yaxis(grid) -> list:
    g = deepcopy(grid)
    size = len(grid)
    for i in range(size):
        for j in range(size // 2):
            g[i][j], g[i][size-1-j] = g[i][size-1-j], g[i][j]
    return g

def flip_xaxis(grid):
    g = deepcopy(grid)
    size = len(grid)
    for i in range(size):
        for j in range(size // 2):
            g[j][i], g[size-1-j][i] = g[size-1-j][i], g[j][i]
    return g

def rotate_45(grid):
    g = deepcopy(grid)
    size = len(grid)
    for i in range(size):
        for j in range(size):
            g[i][j] = grid[size - 1 - j][i]
    return g

def transforms(grid):
    assert len(grid) == len(grid[0])
    return [
        flip_xaxis(grid),
        flip_yaxis(grid),
        rotate_45(grid),
        flip_yaxis(rotate_45(grid)),
        flip_xaxis(rotate_45(grid)),
        rotate_45(rotate_45(grid)),
        flip_xaxis(rotate_45(rotate_45(grid))),
        flip_yaxis(rotate_45(rotate_45(grid))),
        rotate_45(rotate_45(rotate_45(grid))),
        flip_yaxis(rotate_45(rotate_45(rotate_45(grid)))),
        flip_xaxis(rotate_45(rotate_45(rotate_45(grid)))),
    ]

def keyify(grid):
    rows = ["".join(row) for row in grid]
    return "/".join(rows)

lines = [line.strip() for line in open("21.in").readlines()]
rules = dict()
for line in lines:
    left, right = line.split(" => ")
    print(left, right)
    right = [list(row) for row in right.split("/")]
    rules[left] = right


for i in range(18):
    print("iteration", i)
    width = 2 if len(state) % 2 == 0 else 3

    # Each subgrid adds 1 more square to the width
    new_grid_width = len(state) + (len(state) // width)
    new_grid = [[None for _ in range(new_grid_width)] for _ in range(new_grid_width)]

    for i in range(0, len(state), width):
        for j in range(0, len(state), width):
            subgrid = [[state[a][b] for b in range(j, j+width)] for a in range(i, i+width)]
            ts = transforms(subgrid)
            t_grid = None
            for transform in ts:
                if keyify(transform) in rules:
                    t_grid = rules[keyify(transform)]
                    break
            assert t_grid is not None
            
            x = int(j * len(new_grid) / len(state))
            y = int(i * len(new_grid) / len(state))
            for new_y in range(y, y+len(t_grid)):
                for new_x in range(x, x + len(t_grid)):
                    new_grid[new_y][new_x] = t_grid[new_y - y][new_x-x]

    state = new_grid

total = sum([1 if col == "#" else 0 for row in state for col in row])
print(state)
print(total)
