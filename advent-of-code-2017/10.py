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

lengths = list(open("10.in").read().strip())
#lengths = "1,2,3"
lengths = [ord(length) for length in lengths]
lengths.extend([17, 31, 73, 47, 23])

print(lengths)
init = list(range(0, 256))
pos = 0
skip_length = 0

for it in range(64):
    for length in lengths:
        for j in range(length // 2):
            tmp = init[(pos + j) % 256]
            init[(pos + j) % 256] = init[(pos + length - 1 - j) % 256]
            init[(pos + length - 1 - j) % 256] = tmp
        pos += (length + skip_length) % 256
        skip_length += 1
print(init)

xored  = [0] * 16
for i in range(0, 256, 16):
    for j in range(i, i+16):
        xored[i // 16] ^= init[j]

mapping = "0123456789abcdef"
hash = ""
for val in xored:
    first = val >> 4
    second = val & 15
    hash += mapping[first]
    hash += mapping[second]

print(hash)