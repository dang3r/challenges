# https://rosalind.info/problems/grph/

import sys

data = sys.stdin.read().split(">")[1:]
dna = dict()
pref = dict()
for part in data:
    lines = part.splitlines()
    name = lines[0]
    strand = "".join(lines[1:])
    dna[name] = strand
    prefix = strand[:3]
    if prefix not in pref:
        pref[prefix] = []
    pref[prefix].append(name)

for name, strand in dna.items():
    for dna_name in pref.get(strand[-3:], []):
        if name != dna_name:
            print(name, dna_name)
