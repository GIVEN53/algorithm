from sys import stdin

n, m = map(int, stdin.readline().split())
while n != 0 and m != 0:
    arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    ans = 0
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if arr[r - 1][c - 1]:
                dp[r][c] = min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1]) + 1
                ans = max(ans, dp[r][c])
    print(ans)
    n, m = map(int, stdin.readline().split())
