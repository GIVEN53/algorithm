from heapq import heappush, heappop
from queue import PriorityQueue
from sys import stdin


# 1
def dijkstra(start):
    global distance, log

    q = PriorityQueue(maxsize=m)
    q.put((0, start))

    while q.qsize() != 0:
        dist, node = q.get()

        if node == end:
            break

        if distance[node] < dist:
            continue

        for next, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next], log[next] = cost, node
                q.put((cost, next))


n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, stdin.readline().split())

distance = [1e9] * (n + 1)
log = [0] * (n + 1)
dijkstra(start)

print(distance[end])
ans = [end]
while end != start:
    end = log[end]
    ans.append(end)
ans.reverse()

print(len(ans))
print(' '.join(map(str, ans)))


# 2
def dijkstra(start):
    global distance, log

    q = []
    heappush(q, (0, start))

    while q:
        dist, node = heappop(q)

        if node == end:
            break

        if distance[node] < dist:
            continue

        for next, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next], log[next] = cost, node
                heappush(q, (cost, next))


n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, stdin.readline().split())
distance = [1e9] * (n + 1)
log = [0] * (n + 1)

dijkstra(start)

print(distance[end])
ans = [end]
while end != start:
    end = log[end]
    ans.append(end)
ans.reverse()

print(len(ans))
print(' '.join(map(str, ans)))


# 3
def dijkstra(start):
    global distance, log

    q = []
    heappush(q, (0, start))

    while q:
        dist, node = heappop(q)

        if node == end:
            break

        if distance[node] < dist:
            continue

        for next, next_dist in graph[node].items():
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next], log[next] = cost, node
                heappush(q, (cost, next))


n = int(stdin.readline())
m = int(stdin.readline())
graph = [{} for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    if b not in graph[a] or c < graph[a][b]:
        graph[a][b] = c

start, end = map(int, stdin.readline().split())
distance = [1e9] * (n + 1)
log = [0] * (n + 1)

dijkstra(start)

print(distance[end])
ans = [end]
while end != start:
    end = log[end]
    ans.append(end)
ans.reverse()

print(len(ans))
print(' '.join(map(str, ans)))
