from math import inf
lines = [line.strip().split() for line in open("02.in").readlines()]
checksum = 0
for line in lines:
    mn = inf
    mx = -inf
    for num in line:
        num = int(num)
        mn = min(mn, num)
        mx = max(mx, num)
    checksum += mx - mn
print(checksum)

checksum = 0
for line in lines:
    d = dict()
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            mx = max(int(line[i]), int(line[j]))
            mn = min(int(line[i]), int(line[j]))
            if mx % mn == 0:
                checksum += mx / mn
print(checksum)
