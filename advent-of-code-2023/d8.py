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
# Applied the above to it but it was slow
# Something to do with cycles?
# For a given node, if we encounter the same node twice,  we are not guaranteed the
# same instructions again to keep the cycle going.
# Is the cycle guaranteed to have the same length as the number of instructions?
