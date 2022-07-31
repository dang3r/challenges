from collections import Counter

# Taken from https://www.redblobgames.com/grids/hexagons/#coordinates
conv = dict(ne=(1,0,-1), nw=(0, -1, 1), se=(0, 1, -1), sw=(-1,0,1), n=(1, -1, 0), s=(-1, 1, 0))
steps = list(open("11.in").read().strip().split(","))

def dist(vec):
    return sum(abs(el) for el in vec) / 2


def p1(steps):
    c = [conv[step] for step in steps]
    total = (0,0,0)
    mx = 0
    for q, r, s in c:
        total = (total[0] + q, total[1] + r, total[2] + s)
        mx = max(dist(total), mx)
    print("maximum", mx)
    print("distance", dist(total))
    return dist(total)

def binary_reduce(c, op1, op2, term):
    mn = min(c.get(op1), c.get(op2))
    c[op1] -= mn
    c[op2] -= mn
    c[term] += mn

def unary_reduce(c, op1, op2):
    mn = min(c.get(op1), c.get(op2))
    c[op1] -= mn
    c[op2] -= mn

def p1_reduction(steps):
    """Taken from
    https://www.reddit.com/r/adventofcode/comments/7izym2/comment/dr2pzxi/?utm_source=reddit&utm_medium=web2x&context=3

    - This should reduce all of the different vectors to the minimum set needed to reach a given point.
    - Does the order of reduction rules matter?
    - This feels very compilery
    """
    c = Counter(steps)
    unary_reduce(c, "ne", "sw")
    unary_reduce(c, "se", "nw")
    unary_reduce(c, "n", "s")
    binary_reduce(c, "n", "se", "ne")
    binary_reduce(c, "n", "sw", "nw")
    binary_reduce(c, "s", "ne", "se")
    binary_reduce(c, "s", "nw", "sw")
    binary_reduce(c, "nw", "ne", "n")
    binary_reduce(c, "sw", "se", "s")
    total = sum(c.values())
    return total


assert p1("se,sw,se,sw,sw".split(",")) == 3
assert p1("ne,ne,s,s".split(",")) == 2
print(p1(steps))
print(p1_reduction(steps))