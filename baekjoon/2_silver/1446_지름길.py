from sys import stdin

n, d = map(int, stdin.readline().split())
short_road = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

dp = [1e9] * (d + 1)
dp[0] = 0
for i in range(1, d + 1):
    for start, end, length in short_road:
        if i == end and end - start > length:
            dp[i] = min(dp[i], dp[start] + length)
    else:
        dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[-1])

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################
