from sys import stdin


dp = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    dp[1][i] = i

for i in range(2, 31):
    for j in range(i, 31):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while (n := int(stdin.readline())) != 0:
    print(dp[n][n])
