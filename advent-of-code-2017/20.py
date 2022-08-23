from collections import defaultdict
import re

lines = [line.strip() for line in open("20.in").readlines()]
print(len(lines))
bf = None
best_idx = None
particles = {}
formulas = []
for i, line in enumerate(lines):
    rgx = "p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>" 
    match= re.match(rgx, line)
    items = list(map(int,match.groups()))
    particles[i] = items

part2 = True
while True:
    min_i = None
    min_d = None
    for i, p in particles.items():
        p[3] += p[6]
        p[4] += p[7]
        p[5] += p[8]
        p[0] += p[3]
        p[1] += p[4]
        p[2] += p[5]
        d = sum([abs(item) for item in p[:3]])
        if min_i is None or d < min_d:
            min_i = i
            min_d = d

    if part2:
        df = defaultdict(list)
        for i, p in particles.items():
            df[tuple(p[:3])].append(i)

        for k, v in df.items():
            if len(v) > 1:
                print(k,v)
                for u in v:
                    del particles[u]

    if not part2:
        print(min_i)
    else:
        print(len(particles))