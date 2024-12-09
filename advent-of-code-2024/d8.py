lines = open("d8.in").read().splitlines()

from collections import defaultdict

sym_to_coords = defaultdict(list)
for i in range(len(lines)):
    for j in range(len(lines[0])):
        sym = lines[i][j]
        if sym != ".":
            sym_to_coords[sym].append((j, i))

p1_total = set()
p2_total = set()
for sym, coords in sym_to_coords.items():
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            p1 = coords[i]
            p2 = coords[j]
            diff = (p2[0] - p1[0], p2[1] - p1[1])
            candidates = []

            c = p2
            while 0 <= c[0] < len(lines[0]) and 0 <= c[1] < len(lines):
                candidates.append(c)
                c = c[0] + diff[0], c[1] + diff[1]

            c = p2
            while 0 <= c[0] < len(lines[0]) and 0 <= c[1] < len(lines):
                candidates.append(c)
                c = c[0] - diff[0], c[1] - diff[1]

            for c in candidates:
                p1_delta = c[0] - p1[0], c[1] - p1[1]
                p2_delta = c[0] - p2[0], c[1] - p2[1]

                p1_delta = sum(map(abs, p1_delta))
                p2_delta = sum(map(abs, p2_delta))
                if (2 * p1_delta == p2_delta) or (p1_delta == p2_delta * 2):
                    p1_total.add(c)
                p2_total.add(c)
print(len(p1_total))
print(len(p2_total))
