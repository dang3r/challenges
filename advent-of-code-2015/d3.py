vecs = open("d3.in").read()

houses = set([(0, 0)])
pos = (0, 0)
vec_to_d = {
    "<": (-1, 0),
    ">": (1, 0),
    "v": (0, -1),
    "^": (0, 1),
}


def route(vecs):
    houses = set()
    pos = (0, 0)
    for vec in vecs:
        v = vec_to_d[vec]
        pos = (pos[0] + v[0], pos[1] + v[1])
        houses.add(pos)
    return houses


h1 = route(vecs[::2])
h2 = route(vecs[1::2])
h = h1.union(h2)
print(len(h))
