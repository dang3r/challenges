import re
import collections

lines = open("d7.in").read().splitlines()
node_to_deps = collections.defaultdict(list)


def do(lines):
    inst = dict()
    v = dict()

    def transform(m):
        for el in m.groups():
            if el.isdigit():
                inst[el] = lambda el=el: int(el)
        return m.groups()

    for line in lines:
        if m := re.match(r"(\w+) AND (\w+) -> (\w+)", line):
            m = transform(m)
            inst[m[2]] = lambda m=m: v[m[0]] & v[m[1]]
        elif m := re.match(r"(\w+) OR (\w+) -> (\w+)", line):
            m = transform(m)
            inst[m[2]] = lambda m=m: v[m[0]] | v[m[1]]
        elif m := re.match(r"(\w+) LSHIFT (\d+) -> (\w+)", line):
            m = transform(m)
            inst[m[2]] = lambda m=m: v[m[0]] << v[m[1]]
        elif m := re.match(r"(\w+) RSHIFT (\d+) -> (\w+)", line):
            m = transform(m)
            inst[m[2]] = lambda m=m: v[m[0]] >> v[m[1]]
        elif m := re.match(r"NOT (\w+) -> (\w+)", line):
            m = transform(m)
            inst[m[1]] = lambda m=m: ~v[m[0]]
        elif m := re.match("(\w+) -> (\w+)", line):
            m = transform(m)
            inst[m[1]] = lambda m=m: v[m[0]]
        else:
            assert False

        for c in m[:-1]:
            node_to_deps[m[-1]].append(c)

    start = "a"

    def dfs(node, seen):
        if node in seen:
            return
        seen.add(node)
        for descendant in node_to_deps.get(node, []):
            dfs(descendant, seen)
        v[node] = inst[node]()
        v[node] &= 2**16 - 1
        return v[node]

    val = dfs(start, set())
    print(val)


do(lines)
lines.append("956 -> b")
do(lines)
