lines = [line.split(" ") for line in open("10.in").read().splitlines()]
cycle_points = set([20, 60, 100, 140, 180, 220])
total = 0
idx = 0
cycle = 1
X = 1
crt = []


def next_pixel(cycle, X):
    if (cycle - 1) % 40 in set([X - 1, X, X + 1]):
        return "#"
    return "."


for tokens in lines:
    cmd = tokens[0]
    val = int(tokens[1]) if len(tokens) == 2 else 0

    if cmd == "noop":
        crt.append(next_pixel(cycle, X))
        if cycle in cycle_points:
            total += X * cycle
        cycle += 1
    else:
        crt.append(next_pixel(cycle, X))
        crt.append(next_pixel(cycle + 1, X))
        if cycle in cycle_points:
            total += X * (cycle)
        elif cycle + 1 in cycle_points:
            total += X * (cycle + 1)
        cycle += 2
    X += val
print(total)
for idx in range(0, len(crt), 40):
    print("".join(crt[idx : idx + 40]))
