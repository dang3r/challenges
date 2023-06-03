lines = open("02.in").read().splitlines()

depth = 0
forward = 0
for line in lines:
    num = int(line.split(" ")[-1])
    op = line.split()
    if line[0] == "f":
        forward += num
    elif line[0] == "u":
        depth -= num
    elif line[0] == "d":
        depth += num
print(depth * forward)

aim = 0
forward = 0
depth = 0
for line in lines:
    num = int(line.split(" ")[-1])
    op = line.split()
    if line[0] == "f":
        forward += num
        depth += aim * num
    elif line[0] == "u":
        aim -= num
    elif line[0] == "d":
        aim += num
print(depth * forward)
