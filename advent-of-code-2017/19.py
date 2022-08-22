from black import out


maze = [line for line in open("19.in").readlines()]
letters = []
all_letters = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
neighbours = all_letters.union(set("|-_"))
pos = (maze[0].find("|"), 0)
vec = (0, 1)
all_vecs = set([(-1, 0), (0,1), (1,0), (0, -1)])

seen = set()

def in_bounds():
    return 0 <= pos[0] < len(maze[0]) and 0 <= pos[1] < len(maze)

done = False
steps = 0
while True:
    # Find the new corner, or terminate the path
    while maze[pos[1]][pos[0]] != "+":
        # If the path reaches the edge OR if it hits a space, we're done
        # We may hit many `-` or `|` or a letter and continue to proceed despite our direction
        if not in_bounds() or maze[pos[1]][pos[0]] == " ":
            done = True
            break
        pos = (pos[0] + vec[0], pos[1] + vec[1])
        char = maze[pos[1]][pos[0]] 
        steps += 1
        if char in all_letters:
            print(char)
            letters.append(char)
    if done:
        break

    # Find new direction
    possible_vecs = all_vecs.copy()
    possible_vecs.remove((vec[0] * -1, vec[1] * -1))
    for pvec in possible_vecs:
        new_pos = (pos[0] + pvec[0], pos[1] + pvec[1])
        horizontal = pvec[0] != 0
        vertical = not horizontal
        if (maze[new_pos[1]][new_pos[0]] == "-" and horizontal) or (
            maze[new_pos[1]][new_pos[0]] == "|" and vertical
        ):
            steps += 1
            pos = new_pos
            vec = pvec

print("".join(letters))
print(steps)