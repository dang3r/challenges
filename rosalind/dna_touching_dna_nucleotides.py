import sys
from collections import Counter

data = sys.stdin.read()
c = Counter(data)
s = " ".join([str(c[ch]) for ch in "ACGT"])
print(s)
