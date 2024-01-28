from collections import defaultdict

lines = open("d8.in").read().splitlines()
instructions = lines[0]

nodes = {}
for line in lines[1:]:
    node = line[:3]
    left = line[7:10]
    right = line[12:15]
    print(node, left, right)
    nodes[node] = dict(L=left, R=right)

# part 1
idx = 0
point = "AAA"
while point != "ZZZ":
    instruction = instructions[idx % len(instructions)]
    idx += 1
    point = nodes[point][instruction]
print(idx)

# part 2
# - when printing how long it takes to get from ??A -> ??Z from each 1 node, we see that its cyclic. Once you get to that Z, you get back to it
# again after the same number of instructions (not it also takes that # to get there in the first place)
# - once you have a list of cycle lengths, find the least-common-multiple / LCM
# - had to look up how to do GCD


def path(point):
    idx = 0
    yield point
    while True:
        instruction = instructions[idx]
        idx = (idx + 1) % len(instructions)
        point = nodes[point][instruction]
        yield point


a_nodes = [node for node in nodes if node.endswith("A")]
cycle_lengths = []
for a_node in a_nodes:
    print(f"Starting search for {a_node}")
    s = dict()
    for idx, pt in enumerate(path(a_node)):
        if pt in s:
            if pt.endswith("Z"):
                print(pt, s[pt], idx, idx - s[pt])
                cycle_lengths.append(idx - s[pt])
                break
            s[pt] = idx
        elif pt not in s:
            s[pt] = idx

print(cycle_lengths)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    if b > a:
        a, b = b, a
    return (a * b) / (gcd(a, b))


lc = cycle_lengths[0]
for clen in cycle_lengths[1:]:
    lc = lcm(lc, clen)
print(lc)
