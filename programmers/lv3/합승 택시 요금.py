from heapq import heappop, heappush


def dijkstra(start):
    distance[start][start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)

        for next, d in graph[now].items():
            cost = dist + d
            if cost < distance[start][next]:
                distance[start][next] = cost
                heappush(q, (cost, next))


def solution(n, s, a, b, fares):
    global graph, distance

    graph = [{} for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f

    distance = [[1e9] * (n + 1) for _ in range(n + 1)]
    answer = [1e9] * (n + 1)
    for i in range(1, n + 1):
        dijkstra(i)
        answer[i] = distance[i][s] + distance[i][a] + distance[i][b]

    return min(answer)
