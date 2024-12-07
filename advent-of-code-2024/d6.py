maze = [list(line) for line in open("d6.in").read().splitlines()]

vecs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
next_vec = lambda v: vecs[(vecs.index(v) + 1) % len(vecs)]

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] in "^><v":
            pos = (i, j)
            if maze[i][j] == "^":
                vec = -1, 0
            elif maze[i][j] == ">":
                vec = 0, 1
            elif maze[i][j] == "v":
                vec = 1, 0
            elif maze[i][j] == "<":
                vec = 0, -1
original_position = pos
original_vec = vec
seen = set()
while 0 <= pos[0] < len(maze) and 0 <= pos[1] < len(maze[1]):
    seen.add(pos)
    x, y = pos
    new_x, new_y = x + vec[0], y + vec[1]
    if not (0 <= new_x < len(maze) and 0 <= new_y < len(maze[1])):
        break
    if maze[new_x][new_y] == "#":
        vec = next_vec(vec)
        print(vec)
    else:
        pos = (new_x, new_y)

print(len(seen))



candidates = seen.copy()
candidates.remove(original_position)
print("number of candidates", len(candidates))
print(original_position)

total = 0 

for candidate in candidates:
    ox,oy = candidate
    maze[ox][oy] = "#"
    vec = original_vec
    pos = original_position
    seen = set()
    while 0 <= pos[0] < len(maze) and 0 <= pos[1] < len(maze[1]):
        if (vec,pos) in seen:
            total += 1
            break
        seen.add((vec, pos))

        x, y = pos
        new_x, new_y = x + vec[0], y + vec[1]
        if not (0 <= new_x < len(maze) and 0 <= new_y < len(maze[1])):
            break

        if maze[new_x][new_y] == "#":
            vec = next_vec(vec)
        else:
            pos = (new_x, new_y)
    maze[ox][oy] = "."
print(total)

