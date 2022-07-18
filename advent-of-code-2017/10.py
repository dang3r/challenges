lengths = list(map(int, open("10.in").read().strip().split(",")))
init = list(range(0, 256))
pos = 0
skip_length = 0
for length in lengths:
    for j in range(length // 2):
        tmp = init[(pos + j) % 256]
        init[(pos + j) % 256] = init[(pos + length - 1 - j) % 256]
        init[(pos + length - 1 - j) % 256] = tmp
    pos += (length + skip_length) % 256
    skip_length += 1

print(init[0] * init[1])