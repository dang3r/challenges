import re
from collections import Counter

lines = open("d2.in").readlines()
total = len(lines)
good_p1 = 0
good_p2 = 0
for line in lines:
    tokens = line.split(" ")
    mn, mx = list(map(int, tokens[0].split("-")))
    char = tokens[1][0]
    password = tokens[2]
    c = Counter(password)
    good_p1 += int(mn <= c[char] <= mx)

    good_p2 += int((password[mn-1] == char) ^ (password[mx-1] == char))



print(good_p1)
print(good_p2)
