floors = open("d1.in").read()
d = dict()
p = 0
for idx, ch in enumerate(floors):
    p += 1 if ch == "(" else -1
    if p == -1:
        print(idx + 1)
    d[ch] = d.get(ch, 0) + 1

print(d["("] - d[")"])
