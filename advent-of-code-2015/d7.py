import re
import collections

lines = open("d7.in").read().splitlines()
# lines = open("d7.testin").read().splitlines()
node_to_deps = collections.defaultdict(list)


def do(lines):
    d = dict()

    def transform(m):
        for el in m.groups():
            if el.isdigit():
                d[el] = lambda el=el: int(el)
        return m.groups()

    for line in lines:
        if m := re.match(r"(\w+) AND (\w+) -> (\w+)", line):
            m = transform(m)
            d[m[2]] = lambda m=m: d[m[0]] & d[m[1]]
        elif m := re.match(r"(\w+) OR (\w+) -> (\w+)", line):
            m = transform(m)
            d[m[2]] = lambda m=m: d[m[0]] | d[m[1]]
        elif m := re.match(r"(\w+) LSHIFT (\d+) -> (\w+)", line):
            m = transform(m)
            d[m[2]] = lambda m=m: d[m[0]] << d[m[1]]
        elif m := re.match(r"(\w+) RSHIFT (\d+) -> (\w+)", line):
            m = transform(m)
            d[m[2]] = lambda m=m: d[m[0]] >> d[m[1]]
        elif m := re.match(r"NOT (\w+) -> (\w+)", line):
            m = transform(m)
            d[m[1]] = lambda m=m: ~d[m[0]]
        elif m := re.match("(\w+) -> (\w+)", line):
            m = transform(m)
            d[m[1]] = lambda m=m: d[m[0]]
        else:
            assert False

        for c in m[:-1]:
            node_to_deps[m[-1]].append(c)

    ret = []
    start = "a"
    seen = set()

    def dfs(node):
        if node in seen:
            return
        seen.add(node)
        for descendant in node_to_deps.get(node, []):
            dfs(descendant)
        ret.append(node)

    dfs(start)

    for node in ret:
        d[node] = d[node]()
        d[node] &= 2**16 - 1

    print(d[start])


do(lines)
lines.append("956 -> b")
do(lines)
