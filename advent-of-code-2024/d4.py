from collections import defaultdict
maze = open("d4.in").read().splitlines()

maze_d = defaultdict(lambda : defaultdict(str))
for ridx in range(len(maze)):
    maze_d[ridx] = defaultdict(str)
    for cidx in range(len(maze[0])):
        maze_d[ridx][cidx] = maze[ridx][cidx]

def candidates(row, col):
    options = []

    # horizontal
    options.append("".join(maze_d[row][col+i] for i in range(4)))
    options.append("".join(maze_d[row][col-i] for i in range(4)))


    # vertical down
    option = ""
    for i in range(4):
        option += maze_d[row+i][col]
    options.append(option)

    # vertical up
    option = ""
    for i in range(4):
        option += maze_d[row-i][col]
    options.append(option)

    # diagonal down and to the right
    option = ""
    for i in range(4):
        option += maze_d[row+i][col+i]
    options.append(option)

    # down and to left
    option = ""
    for i in range(4):
        option += maze_d[row+i][col-i]
    options.append(option)

    # up and to left
    option = ""
    for i in range(4):
        option += maze_d[row-i][col-i]
    options.append(option)

    # up and to the right 
    option = ""
    for i in range(4):
        option += maze_d[row-i][col+i]
    options.append(option)

    return options


total = 0
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze_d[row][col] == "X":
            cs = candidates(row, col)
            for c in cs:
                if c == "XMAS":
                    total += 1
print(total)

total = 0
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze_d[row][col] == "A":
            corners = "".join([maze_d[row-1][col-1],
                       maze_d[row-1][col+1],
                       maze_d[row+1][col+1],
                       maze_d[row+1][col-1]])
            if len(corners) != 4:
                continue
            print(corners)
            if (corners[:2] == "MM" and corners[2:] == "SS"):
                total += 1
            elif (corners[1:3] == "MM" and corners[3] + corners[0] == "SS"):
                total += 1
            elif (corners[2:] == "MM" and corners[:2] == "SS"):
                total += 1
            elif (corners[3] + corners[0] == "MM" and corners[1:3] == "SS"):
                total += 1
print(total)