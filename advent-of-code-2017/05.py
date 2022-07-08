steps = [int(line.strip()) for line in open("05.in").readlines()]

pos = 0
num_steps = 0
while 0 <= pos < len(steps):
    # TODO: Why didn't this work?
    # pos, steps[pos] = pos + steps[pos], steps[pos] + 1
    tmp = pos
    pos = pos + steps[pos]
    steps[tmp] += 1
    num_steps += 1
print(num_steps)

steps = [int(line.strip()) for line in open("05.in").readlines()]
pos = 0
num_steps = 0
while 0 <= pos < len(steps):
    # TODO: Why didn't this work?
    # pos, steps[pos] = pos + steps[pos], steps[pos] + 1
    tmp = pos
    pos = pos + steps[pos]
    if steps[tmp] >= 3:
        steps[tmp] -= 1
    else:
        steps[tmp] += 1
    num_steps += 1
print(num_steps)
