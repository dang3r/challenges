import functools


def agg(op, vals):
    vals = [int(val) for val in vals]
    if op == "*":
        return functools.reduce(lambda x, y: x * y, vals)
    elif op == "+":
        return functools.reduce(lambda x, y: x + y, vals)


# p1
lines = open("d6.in").read().splitlines()
lines = [line.split() for line in lines]
cols = len(lines[0])
totals = []
for c in range(cols):
    op = lines[-1][c]
    values = [lines[r][c] for r in range(len(lines) - 1)]
    totals += [agg(op, values)]
print(sum(totals))

# p2
lines = open("d6.in").read().splitlines()
lines = [line + " " for line in lines]
st = 0
totals = []
for c in range(len(lines[0])):
    if not all(line[c] == " " for line in lines):
        continue
    segs = [line[st:c] for line in lines]
    st = c + 1

    op = segs[-1].strip()
    sgs = []
    for col in range(len(segs[0])):
        n = ""
        for row in range(len(segs) - 1):
            n += segs[row][col]
        sgs += [int(n)]
    totals += [agg(op, sgs)]

print(sum(totals))
