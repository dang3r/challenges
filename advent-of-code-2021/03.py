lines = open("03.in").read().splitlines()

bits = len(lines[0])
counts = [0 for _ in range(bits)]

for line in lines:
    for i, char in enumerate(line):
        if char == "1":
            counts[i] += 1

gamma = ["1" if count > len(lines) // 2 else "0" for count in counts]
print(gamma)
gamma = int("".join(gamma), 2)
print(gamma)

epsilon = (2**(bits) - 1) ^ gamma
print(2**(bits+1) - 1)
print("{0:b}".format(2**(bits+1) - 1))
print("{0:b}".format(epsilon))

print(gamma * epsilon)


