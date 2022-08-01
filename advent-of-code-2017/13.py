lines = open("13.in").read().split("\n")
line1s = """0: 3
1: 2
4: 4
6: 4""".split("\n")
d = dict()
for line in lines:
    layer, _range = line.split(": ")
    d[int(layer)] = (0, int(_range), 1)

d2 = d.copy()

def update(d):
    for layer, (r_it, rng, dir) in d.items():
        if r_it == rng -1:
            dir = -1
        elif r_it == 0:
            dir = 1
        d[layer] = ((r_it + dir) % rng, rng, dir)

def detected(d, i):
    if i in d and d[i][0] == 0:
        return i * d[i][1]
    return 0

def seen(d, i):
    return i in d and d[i][0] == 0

severity = 0
for i in range(max(d.keys()) + 1):
    severity += detected(d, i)
    update(d)
print(severity)

d = d2
last_layer = max(d.keys())
times = {0:0} #time_to_depth
time_it = 0
done = False
while not done:
    for time in list(times.keys()):
        if seen(d, times[time]):
            del times[time]
            continue
    update(d)
    for time in times:
        times[time] += 1
        if times[time] > last_layer:
            done = True
            print(time)
            break
    time_it += 1
    times[time_it] = 0



