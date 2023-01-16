from heapq import heappop, heappush
from sys import stdin


def bfs(start):
    visited[start] = True
    q = []
    for next in graph[start]:
        heappush(q, next)
    
    min_weight = 0
    while q:
        weight, now = heappop(q)

        if visited[now]:
            continue
        
        min_weight += weight
        visited[now] = True
        for next in graph[now]:
            if not visited[next[1]]:
                heappush(q, next)
    
    return min_weight


V, E = map(int, stdin.readline().split())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

print(bfs(1))
