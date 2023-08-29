from sys import stdin


def dfs(i, visited):
    if dp[i][visited]:
        return dp[i][visited]

    if visited == (1 << n) - 1:
        if w[i][0]:
            return w[i][0]
        return 1e9

    min_cost = 1e9
    for j in range(1, n):
        if not w[i][j] or visited & 1 << j:
            continue
        min_cost = min(min_cost, dfs(j, visited | 1 << j) + w[i][j])

    dp[i][visited] = min_cost
    return dp[i][visited]


n = int(stdin.readline())
w = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0] * (1 << n) for _ in range(n)]
print(dfs(0, 1))

##########################
#    memory: 46676KB     #
#    time:   1052ms      #
##########################
