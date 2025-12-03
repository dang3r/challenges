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
        big = max(big, i * 10 + greatest[idx + 1])
    p1_total += big

print(p1_total)

p2_total = 0
for line in lines:
    length = len(line)
    ints = [int(char) for char in line]

    jolt = ""
    start = 0
    for remaining in range(12, 0, -1):
        end = len(line) - remaining
        seq = ints[start : end + 1]
        mx = max(seq)
        jolt += str(mx)
        start = start + seq.index(mx) + 1

    p2_total += int(jolt)
print(p2_total)
