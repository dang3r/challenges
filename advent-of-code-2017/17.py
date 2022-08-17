steps = 366
pos = 0
buffer = [0]

for num in range(1, 2018):
    pos = (pos + steps) % len(buffer)
    buffer = buffer[:pos + 1] + [num] + buffer[pos+1:]
    pos += 1

print(buffer[(pos+1) % (len(buffer))])

size = 1
pos = 0
val = None
for num in range(1, 50000001):
    pos = (pos + steps) %  size
    if pos == 0:
        val = num
    pos += 1
    size += 1
print(val)