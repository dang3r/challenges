import sys
import functools

data = sys.stdin.read().split(">")[1:]

s_pct = float("-inf")
s_id = None

for segment in data:
    lines = segment.splitlines()
    dna_id = lines[0]
    dna = "".join(lines[1:])
    cg_total = sum(int(x=="G" or x =="C") for x in dna)
    cg_pct = cg_total / len(dna)
    if cg_pct > s_pct:
        s_id = dna_id
        s_pct = cg_pct

print(s_id)
s_pct *= 100
print(f"{s_pct:.6f}")
