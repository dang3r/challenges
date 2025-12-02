lines = open("d1.in").read().splitlines()

start = 50
p1_count = 0
p2_count = 0
for line in lines:
    odeg = int(line[1:])
    rotations = odeg // 100
    odeg %= 100

    new_start = start + odeg if line[0] == "R" else start - odeg
    if start != 0 and (
        (line[0] == "R" and new_start >= 100) or (line[0] == "L" and new_start <= 0)
    ):
        p2_count += 1
    p2_count += rotations

    new_start %= 100
    p1_count += int(new_start == 0)
    start = new_start

print(p1_count)
print(p2_count)
