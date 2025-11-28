from collections import defaultdict


def perms(els):
    if len(els) <= 1:
        yield els

    for i, el in enumerate(els):
        for subperm in perms(els[:i] + els[i + 1 :]):
            yield [el] + subperm


lines = open("d9.in").read().splitlines()
d = defaultdict(dict)
for line in lines:
    tokens = line.split()
    c1, c2, dst = tokens[0::2]
    dst = int(dst)
    d[c1][c2] = dst
    d[c2][c1] = dst

# brute force
cities = list(d.keys())

smallest = float("inf")
largest = float("-inf")
for perm in perms(cities):
    total = 0
    for c1, c2 in zip(perm, perm[1:]):
        total += d[c1][c2]
    smallest = min(smallest, total)
    largest = max(largest, total)

print(smallest)
print(largest)
