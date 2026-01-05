# https://rosalind.info/problems/subs/

import re
import sys

s, t = sys.stdin.read().splitlines()

# straightforward iteration
indices = []
for i in range(len(s)):
    if s[i : i + len(t)] == t:
        indices.append(str(i + 1))

# sol2: use regex lookaheads
rindices = [str(m.start() + 1) for m in re.finditer(f"(?={t})", s)]
assert rindices == indices

print(" ".join(indices))
