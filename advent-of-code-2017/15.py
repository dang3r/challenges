values = [634, 301]
factors = [16807, 48271]
divisor = 2147483647
bottom_16 = lambda x: x & (2**16-1)

same = 0
for i in range(int(4e7)):
    if (i % 1000000) == 0:
        print(i)
    values = [value*factors[i] % divisor for i, value in enumerate(values)]
    if bottom_16(values[0]) == bottom_16(values[1]):
        same += 1
print(same)


def next_values(start_value, coefficient, divisor, multiple):
    value = start_value
    while True:
        value = (value * coefficient) % divisor
        if (value % multiple) == 0:
            yield value
        
same = 0
values = [634, 301]
g1 = next_values(values[0], factors[0], divisor, 4)
g2 = next_values(values[1], factors[1], divisor, 8)
for i in range(int(5e6)):
    if (i % 1000000) == 0:
        print(i)
    v1 = next(g1)
    v2 = next(g2)
    if bottom_16(v1) == bottom_16(v2):
        same += 1
print(same)