
class UnionFind:
    def __init__(self):
        self.parents = {}

    def find(self, a):
        if self.parents[a] != a:
            return self.find(self.parents[a])
        return a

    def union(self, a, b):
        self._add_node(a)
        self._add_node(b)
        self.parents[self.find(a)] = self.find(b)

    def _add_node(self, a):
        if a not in self.parents:
            self.parents[a] = a

    def size(self, a):
        par = self.find(a)
        total = 0
        for k in self.parents:
            if self.find(k) == par:
                total += 1
        return total

    def groups(self):
        s = set()
        for k in self.parents:
            s.add(self.find(k))
        return len(s)

uf = UnionFind()
lines = list(open("12.in").read().split("\n"))
for line in lines:
    left, right = line.split(" <-> ")
    for digit in right.split(","):
        uf.union(left, digit.strip())

print(uf.size('0'))
print(uf.groups())