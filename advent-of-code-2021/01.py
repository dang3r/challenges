depths = [int(line) for line in open("01.in").read().splitlines()]

total = sum(1 if d1 > d0 else 0 for d0, d1 in zip(depths, depths[1:]))
print(total)

window_size = 3
agg_depths = [sum(depths[i:i+3]) for i in range(len(depths )- 2)]
total = sum(1 if d1 > d0 else 0 for d0, d1 in zip(agg_depths, agg_depths[1:]))
print(total)
