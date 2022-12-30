from collections import defaultdict
import heapq
import re

lines = open("16.in").read().splitlines()

valve_to_flow = dict()
graph = defaultdict(list)

for line in lines:
    m = re.search(
        "^Valve (?P<valve>[A-Z]{2}) has flow rate=(?P<flow_rate>\d+); tunnel[s]? lead[s]? to valve[s]? (?P<edges>.*)$",
        line,
    )
    valve_to_flow[m.group("valve")] = int(m.group("flow_rate"))
    edges = m.group("edges").split(", ")
    for edge in edges:
        graph[m.group("valve")].append(edge)


def dijkstra(graph, src, dst):
    nodes = list(graph.keys())
    dist = {node: float("inf") for node in nodes}
    dist[src] = 0
    prev = {pos: None for pos in nodes}
    q = []
    for node in nodes:
        heapq.heappush(q, (dist[node], node))

    while q:
        src_to_node_dist, node = heapq.heappop(q)
        if node == dst:
            break
        for adj_node in graph[node]:
            adj_node_dist = dist[node] + 1
            if adj_node_dist < dist[adj_node]:
                dist[adj_node] = adj_node_dist
                prev[adj_node] = node
                done = False
                for i in range(len(q)):
                    _, _node = q[i]
                    if _node == adj_node:
                        done = True
                        q[i] = (adj_node_dist, adj_node)
                        heapq.heapify(q)
                        break
                if not done:
                    raise Exception("LOL")
    return dist[dst]


g = {}
nodes_with_flow = ["AA"] + sorted(
    [node for node, flow in valve_to_flow.items() if flow > 0]
)
for i in range(len(nodes_with_flow)):
    for j in range(i + 1, len(nodes_with_flow)):
        g[f"{nodes_with_flow[i]}_{nodes_with_flow[j]}"] = dijkstra(
            graph, nodes_with_flow[i], nodes_with_flow[j]
        )

q = [(["AA"], set(), 0, 0)]
mx = float("-inf")
print(g)

while q:
    path, open, time, total = q.pop(0)
    new_flow = sum(valve_to_flow[valve] for valve in open)
    print(path, open, time, total, new_flow)
    if time >= 30:
        continue
    total += new_flow
    print(path, open, time, total, new_flow)
    mx = max(mx, total)

    # Open current valve if it has flow
    open.add(path[-1])
    if valve_to_flow[path[-1]] > 0:
        time += 1
    print(path, open, time, total)

    # Find nodes with flow that have not been visited before
    current_node = path[-1]
    candidates = []
    for edge in g:
        n1, n2 = sorted(edge.split("_"))
        if current_node in edge:
            other = n1 if n1 != current_node else n2
            if other not in open:
                candidates.append(other)

    new_flow = sum(valve_to_flow[valve] for valve in open)
    for next_node in candidates:
        key = "_".join(sorted([path[-1], next_node]))
        time_taken = g[key]
        new_path = list(path) + [next_node]
        new_open = set(open)
        new_total = total + time_taken * new_flow
        if time + time_taken >= 30:
            mx = max(mx, total + (30 - time) * new_flow)
        q.append((new_path, new_open, time + time_taken, new_total))

    # If we still have time, but there we've visited every node
    if not candidates:
        print("OPENED ALL")
        mx = max(mx, total + (30 - time) * new_flow)

print(mx)
