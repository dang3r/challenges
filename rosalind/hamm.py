# https://rosalind.info/problems/hamm/
#
#
import sys

dna1, dna2 = sys.stdin.read().splitlines()

diffs = sum(int(d1 != d2) for d1, d2 in zip(dna1, dna2))
print(diffs)
