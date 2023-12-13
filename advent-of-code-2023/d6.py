lines = open("d6.in").read().splitlines()

times = [int(val) for val in lines[0].split()[1:]]
distances = [int(val) for val in lines[1].split()[1:]]

# Part 1
ways = []
for time, distance in zip(times, distances):
    ways.append(0)
    for i in range(0, time + 1):
        distance_travelled = i * (time - i)
        if distance_travelled > distance:
            ways[-1] += 1

product = 1
for way in ways:
    product *= way
print(product)

# Part 2
time = int("".join(str(time) for time in times))
distance = int("".join(str(d) for d in distances))
ways = 0
for i in range(0, time + 1):
    distance_travelled = i * (time - i)
    if distance_travelled > distance:
        ways += 1
print(ways)
