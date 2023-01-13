from collections import deque
from sys import stdin, setrecursionlimit


# 1
def bfs(x, y):
    global visited

    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        if (x, y) not in graph:
            continue

        for i in range(4):
            a = x + row[i]
            b = y + col[i]

            if a > -1 and a < M and b > -1 and b < N and not visited[a][b]:
                visited[a][b] = True
                q.append((a, b))


row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]
T = int(stdin.readline())

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    graph = set()
    visited = [[False] * N for _ in range(M)]

    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        graph.add((X, Y))

    cnt = 0
    for now in graph:
        x = now[0]
        y = now[1]
        if not visited[x][y]:
            bfs(x, y)
            cnt += 1
    print(cnt)


# 2
def dfs(x, y):
    global visited

    visited[x][y] = True
    near = []
    for i in range(4):
        a = x + row[i]
        b = y + col[i]

        if a > -1 and a < M and b > -1 and b < N and not visited[a][b]:
            near.append((a, b))

    for x, y in near:
        if visited[x][y] or (x, y) not in graph:
            continue

        dfs(x, y)


row = [0, 0, -1, 1]
col = [-1 , 1, 0, 0]
setrecursionlimit(10**6)
T = int(stdin.readline())

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    graph = set()
    visited = [([False] * N) for _ in range(M)]

    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        graph.add((X, Y))
    
    cnt = 0
    for now in graph:
        x = now[0]
        y = now[1]
        if not visited[x][y]:
            dfs(x, y)
            cnt += 1
    print(cnt)