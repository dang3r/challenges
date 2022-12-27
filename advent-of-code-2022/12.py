import heapq

grid = [list(line) for line in open("12.in").read().splitlines()]
in_bounds = lambda pos: (0 <= pos[0] < len(grid)) and (0 <= pos[1] < len(grid[0]))
char = lambda pos: grid[pos[0]][pos[1]]
vecs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dst = src = None
starts = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "E":
            dst = (i, j)
            grid[i][j] = "{"
        if grid[i][j] == "S":
            src = (i, j)
            grid[i][j] = "a"
        if grid[i][j] == "a":
            u = (i, j)
            for vec in vecs:
                v = (u[0] + vec[0], u[1] + vec[1])
                if in_bounds(v) and char(v) == "b":
                    starts.append(u)


def dijkstra(grid, src, dst):
    coords = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
    dist = {pos: float("inf") for pos in coords}
    dist[src] = 0
    prev = {pos: None for pos in coords}
    q = []
    for coord in coords:
        heapq.heappush(q, (dist[coord], coord))

    while q:
        _, u = heapq.heappop(q)
        if u == dst:
            break
        for vec in vecs:
            v = (u[0] + vec[0], u[1] + vec[1])
            if in_bounds(v) and (ord(char(v)) <= ord(char(u)) + 1):
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    done = False
                    for i in range(len(q)):
                        _, coord = q[i]
                        if coord == v:
                            done = True
                            q[i] = (alt, v)
                            heapq.heapify(q)
                            break
                    if not done:
                        raise Exception("LOL")
    return dist[dst]


dist = dijkstra(grid, src, dst)
print(dist)
print(len(starts))
for start in starts:
    print(dijkstra(grid, start, dst))
