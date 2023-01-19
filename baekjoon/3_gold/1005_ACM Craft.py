from collections import deque
from sys import stdin


def topological_sort(target):
    global in_degree

    q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    dp = [0] * (N + 1)
    while q:
        now = q.popleft()
        dp[now] += time[now - 1]

        if now == target:
            return dp[now]

        for next in graph[now]:
            in_degree[next] -= 1
            dp[next] = max(dp[now], dp[next])
            if in_degree[next] == 0:
                q.append(next)


T = int(stdin.readline())
for _ in range(T):
    N, K = map(int, stdin.readline().split())
    time = [*map(int, stdin.readline().split())]
    graph = [[] for _ in range(N + 1)]

    in_degree = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        in_degree[b] += 1

    W = int(stdin.readline())
    print(topological_sort(W))
