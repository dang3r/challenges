import sys

d = dict(A="T",T="A",C="G",G="C")
dna = sys.stdin.read().strip()

rc = "".join([d[el] for el in dna[::-1]])
print(rc)

