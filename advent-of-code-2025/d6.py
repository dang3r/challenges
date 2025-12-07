lines = open("d6.in").read().splitlines()
lines = [line.split() for line in lines]
cols = len(lines[0])

# p1
totals = []
for c in range(cols):
    op = lines[-1][c]
    start = int(lines[0][c])
    do = lambda val: start * int(val) if op == "*" else start + int(val)
    for r in range(1, len(lines) - 1):
        start = do(lines[r][c])
    totals += [start]

print(sum(totals))

# p2
# added newline to end of last line to make partitioning easier
lines = open("d6.in").readlines()
st = 0
totals = []
for c in range(len(lines[0])):
    if not all(lines[row][c] in [" ", "\n"] for row in range(len(lines))):
        continue
    segs = [row[st:c] for row in lines]
    st = c + 1

    op = segs[-1].strip()
    rows = len(segs) - 1
    cols = len(segs[0])
    sgs = []
    for col in range(cols):
        n = ""
        for row in range(rows):
            n += segs[row][col]
        sgs += [int(n)]

    start = int(sgs[0])
    do = lambda val: start * int(val) if op == "*" else start + int(val)
    for r in range(1, len(sgs)):
        start = do(sgs[r])
    totals += [start]

print(sum(totals))
