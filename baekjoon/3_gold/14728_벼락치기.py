from sys import stdin

n, t = map(int, stdin.readline().split())
dp = [0] * (t + 1)

for _ in range(n):
    k, s = map(int, stdin.readline().split())
    for i in range(t, k - 1, -1):
        dp[i] = max(dp[i], dp[i - k] + s)

print(dp[t])

##########################
#    memory: 31256KB     #
#    time:   368ms       #
##########################
