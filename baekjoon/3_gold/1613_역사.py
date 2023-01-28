from sys import stdin


# 1 Floyd-Warshall
n, k = map(int, stdin.readline().split())
graph = [[1e9] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = -1
    graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] ==  1e9 or graph[k][j] == 1e9:
                continue

            if graph[i][k] + graph[k][j] > 1:
                graph[i][j] = 1
            elif graph[i][k] + graph[k][j] < -1:
                graph[i][j] = -1
            else:
                graph[i][j] = min(graph[i][j], 1e9)
            
s = int(stdin.readline())
for _ in range(s):
    start, end = map(int, stdin.readline().split())
    if graph[start][end] == 1e9:
        print(0)
    else:
        print(graph[start][end])


# 2 dfs
def dfs(start):
    global event, visited
    if visited[start]:
        return

    visited[start] = True
    for next in graph[start]:
        dfs(next)
        event[start].add(next)
        event[start] |= event[next]


n, k = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

event = [set() for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(1, n + 1):
    dfs(i)

s = int(stdin.readline())
for _ in range(s):
    start, end = map(int, stdin.readline().split())
    if end in event[start]:
        print(-1)
    elif start in event[end]:
        print(1)
    else:
        print(0)
