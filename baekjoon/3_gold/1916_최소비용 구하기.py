from sys import stdin
from heapq import heappop, heappush


def dijkstra(start):
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)
        if now == end:
            break

        for next, next_dist in city[now].items():
            next_dist += dist
            if next_dist < distance[next]:
                distance[next] = next_dist
                heappush(q, (next_dist, next))


n, m = int(stdin.readline()), int(stdin.readline())
city = [{} for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, stdin.readline().split())
    if b in city[a]:
        city[a][b] = min(city[a][b], cost)
    else:
        city[a][b] = cost

start, end = map(int, stdin.readline().split())

distance = [1e9] * (n + 1)
dijkstra(start)

print(distance[end])

##########################
#    memory: 38400KB     #
#    time:   196ms       #
##########################
