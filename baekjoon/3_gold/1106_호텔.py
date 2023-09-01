from sys import stdin

c, n = map(int, stdin.readline().split())
city = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [1e9] * (c + 1)
dp[0] = 0

for i in range(1, c + 1):
    for cost, customer in city:
        if i <= customer:
            dp[i] = min(dp[i], cost)
        else:
            dp[i] = min(dp[i], dp[i - customer] + cost)

print(dp[-1])

##########################
#    memory: 31256KB     #
#    time:   52ms        #
##########################
