from collections import defaultdict
import re

lines = [line.strip() for line in open("07.in").readlines()]
state = defaultdict(list)
n_to_children = defaultdict(list)
n_to_weight = dict()
it = None

for line in lines:
    m = re.match(r'(?P<key>\w+) \((?P<weight>\d+)\)( -> (?P<children>.*))?', line)
    if m:
        d = m.groupdict()
        key = d['key']
        weight = d['weight']
        n_to_weight[key] = int(weight)
        if d['children'] is not None:
            children = [s.strip() for s in d['children'].split(',')]
            n_to_children[key] = children
            for child in children:
                state[child].append(key)
            it = key

while it in state:
    it = state[it][0]
print(it)

def check(root):
    w = n_to_weight[root]
    chw = [check(child) for child in n_to_children[root]]
    ws = [w[2] for w in chw]
    if len(set(ws)) > 1:
        print(root)
        mn = min(ws)
        mx = max(ws)
        diff = abs(mx - mn)
        if ws.count(mn) > ws.count(mx):
            dx = ws.index(mx)
            print(chw[dx][1] - diff)
        else:
            dx = ws.index(mn)
            print(chw[dx][1] + diff)
    return root, w, sum(ws) + w

check(it)
