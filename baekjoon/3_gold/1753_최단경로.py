from sys import stdin
from heapq import heappop, heappush


def dijkstra(start):
    distances = [1e9] * (V + 1)
    distances[start] = 0
    q = []
    heappush(q, (distances[start], start))

    while q:
        dist, now = heappop(q)
        if distances[now] < dist:
            continue

        for next, next_dist in graph[now]:
            distance = dist + next_dist
            if distance < distances[next]:
                distances[next] = distance
                heappush(q, (distance, next))

    return distances


V, E = map(int, stdin.readline().split())
K = int(stdin.readline())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

distances = dijkstra(K)
for dist in distances[1:]:
    print("INF" if dist == 1e9 else dist)

##########################
#    memory: 68516KB     #
#    time:   652ms       #
##########################
