banks = list(map(int, "14	 0	15	12	11	11	3	5	1	6	8	4	9	1	8	4".split()))
s = set()
d = dict()
count = 0
while tuple(banks) not in s:
    d[tuple(banks)] = count
    s.add(tuple(banks))
    most = max(banks)
    idx = banks.index(most)
    banks[idx] = 0
    while most > 0:
        idx = (idx + 1) % len(banks)
        banks[idx] += 1
        most -= 1
    count += 1


print(count)
print(count - d[tuple(banks)])