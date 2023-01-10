lines = open("18.in").read().splitlines()
positions = [tuple(map(int, line.split(","))) for line in lines]

vecs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)]
sides = 0
seen = set()
for pos in positions:
    for vec in vecs:
        new_pos = tuple(pos[i] + vec[i] for i in range(len(pos)))
        if new_pos not in seen:
            sides += 1
        else:
            sides -= 1

    seen.add(pos)
print(sides)
