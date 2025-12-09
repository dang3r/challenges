from collections import Counter
import functools

lines = open("d8.in").read().splitlines()
lines = [tuple(map(int,line.split(","))) for line in lines]
distance = lambda a,b: sum((a[i]-b[i])**2 for i in range(len(a))) ** 0.5


d = dict()
for i, pt1 in enumerate(lines):
    for j, pt2 in enumerate(lines[i+1:]):
        k = tuple(sorted(tuple([pt1, pt2])))
        d[k] = distance(pt1, pt2)


uf = {line:line for line in lines}
def find(pt):
    if uf[pt] == pt:
        return pt
    root = find(uf[pt])
    uf[pt] = root
    return root

def union(pt1, pt2):
    r1 = find(pt1)
    r2 = find(pt2)
    uf[r2] = r1

def part1():
    sorted_pairs = sorted(d.items(), key=lambda kv: kv[1])[:1000]
    for (pt1, pt2), dist in sorted_pairs:
        union(pt1, pt2)

    for k in uf:
        find(k)

    c = Counter(uf.values()).most_common(3)
    total = functools.reduce(lambda x,y:x*y, [v[1] for v in c], 1)
    print(c)
    print(total)

def part2():
    sorted_pairs = sorted(d.items(), key=lambda kv: kv[1])
    
    for (pt1, pt2), dist in sorted_pairs:
        union(pt1, pt2)
        for k in uf:
            find(k)
        if len(set(uf.values())) == 1:
            print(pt1[0] * pt2[0])
            break

part1()
part2()

