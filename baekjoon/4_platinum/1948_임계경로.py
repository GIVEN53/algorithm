from collections import deque
from sys import stdin


def topological_sort(start):
    global distance, max_dist_edges

    q = deque()
    q.append((start, 0))
    while q:
        node, dist = q.popleft()

        for next, next_dist in graph[node].items():
            in_degree[next] -= 1
            cost = dist + next_dist
            if distance[next] < cost:
                distance[next] = cost
                max_dist_edges[next] = [node]
            elif distance[next] == cost:
                max_dist_edges[next].append(node)

            if in_degree[next] == 0:
                q.append((next, distance[next]))


def get_edge_cnt(start):
    q = deque([start])
    edges = set()
    while q:
        node = q.popleft()

        for next in max_dist_edges[node]:
            if (node, next) not in edges:
                edges.add((node, next))
                q.append(next)

    return len(edges)


n, m = int(stdin.readline()), int(stdin.readline())
graph = [{} for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
    s, e, t = map(int, stdin.readline().split())
    graph[s][e] = t
    in_degree[e] += 1
start, end = map(int, stdin.readline().split())

distance = [0] * (n + 1)
max_dist_edges = [[] for _ in range(n + 1)]
topological_sort(start)

print(distance[end])
print(get_edge_cnt(end))
