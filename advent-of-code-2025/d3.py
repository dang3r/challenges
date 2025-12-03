from collections import defaultdict

lines = open("d3.in").read().splitlines()

p1_total = 0
for line in lines:
    ints = [int(char) for char in line]

    mx = -1
    greatest = []
    for i in ints[::-1]:
        if i > mx:
            mx = i
        greatest.append(mx)
    greatest = greatest[::-1]

    big = -1
    for idx, i in enumerate(ints[:-1]):
        if i * 10 + greatest[idx] > big:
            big = i * 10 + greatest[idx + 1]
    p1_total += big

print(p1_total)

p2_total = 0
for line in lines:
    length = len(line)
    ints = [int(char) for char in line]
    d = defaultdict(list)
    for idx, i in enumerate(ints):
        d[i].append(idx)

    jolt = ""
    indexes = [0]
    while indexes:
        idx = indexes.pop()
        found = False
        for num in sorted(d.keys(), key=lambda x: -x):
            if found:
                break
            for nidx in list(d[num]):
                if (
                    nidx >= idx
                    and len(jolt) != 12
                    and (len(line) - nidx) >= (12 - len(jolt))
                ):
                    jolt += str(num)
                    indexes.append(nidx + 1)
                    found = True
                    break
    p2_total += int(jolt)
print(p2_total)
