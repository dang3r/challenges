import string

lines = [line.strip() for line in open("03.in").readlines()]
char_to_val = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1)))

total = 0
for line in lines:
    c1, c2 = line[: len(line) // 2], line[len(line) // 2 :]
    el = set(c1) & set(c2)
    assert len(list(el)) == 1
    total += char_to_val[list(el)[0]]
print(total)

total = 0
for idx in range(0, len(lines), 3):
    g1, g2, g3 = lines[idx : idx + 3]
    inter = list(set(g1) & set(g2) & set(g3))
    assert len(inter) == 1
    total += char_to_val[inter[0]]
print(total)
