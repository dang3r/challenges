import sys

digits = open("01.in").read()
digits += digits[0]
p1_total = 0
for i in range(len(digits) - 1):
    if digits[i] == digits[i+1]:
        p1_total += int(digits[i])
print(p1_total)

p2_total = 0
for i in range(len(digits) // 2):
    if digits[i] == digits[i + len(digits) // 2]:
        p2_total += int(digits[i]) * 2
print(p2_total)

