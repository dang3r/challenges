lines = [line.strip() for line in open("04.in", "r").readlines()]

p1_total = 0
p2_total = 0
for line in lines:
    sections = [list(map(int, line.split("-"))) for line in line.split(",")]
    sec = sorted(sections, key=lambda sec: sec[0])
    if (sec[1][0] <= sec[0][1] and sec[1][1] <= sec[0][1]) or (
        sec[1][0] == sec[0][0] and sec[0][1] <= sec[1][1]
    ):
        p1_total += 1
        p2_total += 1
    elif sec[0][0] <= sec[1][0] <= sec[0][1]:
        p2_total += 1
print(p1_total)
print(p2_total)
