from sys import stdin

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for cnt in range(1, n):
    for i in range(n - cnt):
        j = i + cnt
        if cnt == 1:
            dp[i][j] = arr[i][0] * arr[j][0] * arr[j][1]
            continue
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j],
                dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k + 1][0] * arr[j][1],
            )

print(dp[0][n - 1])

##########################
#    PyPy3               #
#    memory: 117412KB    #
#    time:   824ms       #
##########################
