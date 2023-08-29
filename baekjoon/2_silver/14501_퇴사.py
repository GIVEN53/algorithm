from sys import stdin

n = int(stdin.readline())
consulting = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    day, price = consulting[i]
    if i + day > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + day] + price, dp[i + 1])

print(dp[0])

##########################
#    memory: 31256KB     #
#    time:   40ms        #
##########################
