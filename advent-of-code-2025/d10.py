lines = open("d10.in").read().splitlines()
data = []
for line in lines:
    tokens = line.split(" ")
    lights = [int(c=='#') for c in tokens[0][1:-1]]
    buttons = []
    for t in tokens[1:-1]:
        default = [0 for _ in lights]
        for i in t[1:-1].split(","):
            default[int(i)] = 1
        buttons.append(default)

    jolts = [0 for _ in lights]
    for i, t in enumerate(tokens[-1][1:-1].split(",")):
        jolts[i] = int(t)

    data.append((lights, buttons, jolts))

total = 0
for lights, buttons, jolts in data:
    presses = float("inf")
    for c in range(2**len(buttons)):
        default = [0 for _ in lights]
        p = 0
        for i, bt in enumerate(buttons):
            if c & (2**i):
                p += 1
                default = [(default[j] + bt[j]) % 2 for j in range(len(lights))] 
        assert all(v == 0 or v == 1 for v in default)
        if default == lights:
            presses = min(presses, p)
    total += presses
print(total)


total = 0
for lights, buttons, jolts in data:
    presses = float("inf")
    for c in range(2**len(buttons)):
        default = [0 for _ in lights]
        p = 0
        for i, bt in enumerate(buttons):
            if c & (2**i):
                p += 1
                default = [(default[j] + bt[j]) % 2 for j in range(len(lights))] 
        assert all(v == 0 or v == 1 for v in default)
        if default == lights:
            presses = min(presses, p)
    total += presses
print(total)




