from heapq import heappop, heappush
from sys import stdin


def dijkstra(start):
    distance = [1e9] * (N + 1)
    distance[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        dist, node = heappop(q)
        if distance[node] < dist:
            continue

        for next, next_dist in graph[node].items():
            cost = next_dist + dist
            if cost < distance[next]:
                distance[next] = cost
                heappush(q, (cost, next))

    return distance


N, E = map(int, stdin.readline().split())
graph = [{} for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c
u, v = map(int, stdin.readline().split())

distance_1 = dijkstra(1)
distance_u = dijkstra(u)
distance_v = dijkstra(v)

u_first = distance_1[u] + distance_u[v] + distance_v[N]
v_first = distance_1[v] + distance_v[u] + distance_u[N]
min_distance = min(u_first, v_first)
print(min_distance if min_distance < 1e9 else -1)
