from collections import deque
from sys import stdin


def dfs(start):
    global visited, dfs_ans

    visited[start] = True
    dfs_ans.append(start)

    for next in graph[start]:
        if not visited[next]:
            dfs(next)


def bfs(start):
    global visited, bfs_ans

    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        bfs_ans.append(now)

        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


N, M, V = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

dfs_ans = []
visited = [False] * (N + 1)
dfs(V)

bfs_ans = []
visited = [False] * (N + 1)
bfs(V)

print(*dfs_ans)
print(*bfs_ans)
