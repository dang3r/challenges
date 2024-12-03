from collections import Counter

lines = open("d1.in").read().splitlines()

left = []
right = []

for line in lines:
    n1, n2 = line.split()
    left.append(int(n1))
    right.append(int(n2))

left = sorted(left)
right = sorted(right)
total = 0

# P1
for l, r in zip(left,right):
    total += abs(l-r)
print(total)

# P2
prod_total = 0
c = Counter(right)
for item in set(left):
    prod_total += item * c.get(item, 0)
print(prod_total)
