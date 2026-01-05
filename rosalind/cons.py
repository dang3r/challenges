# https://rosalind.info/problems/cons/

import sys

data = sys.stdin.read().split(">")[1:]
dna = []
for d in data:
    lines = d.splitlines()
    dna.append("".join(lines[1:]))
len_strand = len(dna[1])

profile = {k: [0] * len_strand for k in "ACGT"}
for i in range(len_strand):
    for strand in dna:
        profile[strand[i]][i] += 1

agg = ""
for i in range(len_strand):
    highest = max("ACGT", key=lambda n: profile[n][i])
    agg += highest

print(agg)
for key in "ACTG":
    print(f"{key}: ", end=" ")
    print(" ".join(str(i) for i in profile[key]))
