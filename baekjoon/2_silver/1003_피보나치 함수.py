from sys import stdin


def fibonacci(n):
    global dp
    if n <= 1 or (dp[n][0] and dp[n][1]):
        return

    fibonacci(n - 1)
    fibonacci(n - 2)
    dp[n][0] = dp[n - 1][0] + dp[n - 2][0]
    dp[n][1] = dp[n - 1][1] + dp[n - 2][1]
    return


T = int(stdin.readline())
dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for _ in range(T):
    n = int(stdin.readline())
    fibonacci(n)
    print(dp[n][0], dp[n][1])
