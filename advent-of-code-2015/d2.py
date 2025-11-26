lines = open("d2.in").read().splitlines()
sides = [list(map(int, line.split("x"))) for line in lines]

total = 0
ribbon_total = 0
for w, h, l in sides:
    r = 2 * w * l + 2 * w * h + 2 * l * h
    s1, s2 = sorted([w, h, l])[:2]
    total += r
    total += s1 * s2
    ribbon_total += w * h * l
    ribbon_total += 2 * s1 + 2 * s2

print(total)
print(ribbon_total)
