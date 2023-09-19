from sys import stdin

n, m = map(int, stdin.readline().split())
memories = [*map(int, stdin.readline().split())]
costs = [*map(int, stdin.readline().split())]

total_cost = sum(costs)
dp = [[0] * (total_cost + 1) for _ in range(n + 1)]
res = 1e9
for i in range(1, n + 1):
    for j in range(1, total_cost + 1):
        dp[i][j] = dp[i - 1][j]
        if costs[i - 1] <= j:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - costs[i - 1]] + memories[i - 1])
        if dp[i][j] >= m:
            res = min(res, j)

print(res)

##########################
#    memory: 48028KB     #
#    time:   808ms       #
##########################
