# https://rosalind.info/problems/fibd/


import sys

intify = lambda x: [int(el) for el in x]
n, m = intify(sys.stdin.read().split())

rabbits = [0 for _ in range(n)]
ages = dict()
for month in range(n):
    if month == 0:
        ages = {0: 1}
    else:
        ages = {age + 1: count for age, count in ages.items()}
        ages[0] = sum(count for age, count in ages.items() if 1 < age <= m)
        ages = {age: count for age, count in ages.items() if age < m}
    rabbits[month] = sum(ages.values())
print(rabbits[-1])
