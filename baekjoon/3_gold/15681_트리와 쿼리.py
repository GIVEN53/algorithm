from sys import stdin, setrecursionlimit


def dfs(start):
    global dp, visited

    visited[start] = True
    for next in tree[start]:
        if not visited[next]:
            dfs(next)
            dp[start] += dp[next]


setrecursionlimit(10 ** 6)
N, R, Q = map(int, stdin.readline().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [1] * (N + 1)
visited = [False] * (N + 1)
dfs(R)

for _ in range(Q):
    sub_root = int(stdin.readline())
    print(dp[sub_root])
