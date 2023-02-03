from sys import stdin, setrecursionlimit


def dfs(now):
    global dp, visited

    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            dfs(next)
            dp[now][0] += dp[next][1]
            dp[now][1] += min(dp[next][0], dp[next][1])


setrecursionlimit(10 ** 6)
N = int(stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 1] for _ in range(N + 1)]
visited = [False] * (N + 1)

dfs(1)
print(min(dp[1][0], dp[1][1]))
