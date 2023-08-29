from sys import stdin


n = int(stdin.readline())
mod = 1000000000
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(1 << 10):
            if j > 0:
                dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
            if j < 9:
                dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]

print(sum(dp[n][i][(1 << 10) - 1] for i in range(10)) % mod)

##########################
#    memory: 39604KB     #
#    time:   628ms       #
##########################
