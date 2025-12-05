
ranges = []
ingredients = []
for line in open("d5.in").read().splitlines():
    if "-" in line:
        ranges.append(tuple(map(int, line.split("-"))))
    elif line:
        ingredients.append(int(line))

ranges = sorted(ranges, key=lambda r: r[0])

fresh = 0
for i in ingredients:
    for r1,r2 in ranges:
        if r1 <= i <= r2:
            fresh +=1
            break
        elif r1 > i:
            break
print(fresh)

fresh_ids = 0
for c, (cs, ce) in enumerate(ranges):
    enclosed = False
    for p, (ps, pe) in enumerate(ranges[:c]):
        if ps <= cs <= pe:
            if ps <= ce <= pe:
                enclosed = True
                break
            cs = pe + 1
    if not enclosed:
        fresh_ids += ce - cs + 1
print(fresh_ids)


