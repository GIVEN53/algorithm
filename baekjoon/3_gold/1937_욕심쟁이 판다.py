from sys import stdin, setrecursionlimit


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    next_cnt = 1
    for i in range(4):
        nx = x + direction[i]
        ny = y + direction[3 - i]

        if is_out_of_range(nx, ny) or forest[x][y] >= forest[nx][ny]:
            continue

        next_cnt = max(next_cnt, dfs(nx, ny) + 1)

    dp[x][y] = next_cnt
    return dp[x][y]


def is_out_of_range(x, y):
    return x < 0 or x > n - 1 or y < 0 or y > n - 1


setrecursionlimit(10 ** 6)
n = int(stdin.readline())
forest = [[*map(int, stdin.readline().split())] for _ in range(n)]

direction = [0, 0, 1, -1]
dp = [[0] * n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        if dp[i][j]:
            continue
        dp[i][j] = dfs(i, j)
        ans = max(ans, dp[i][j])

print(ans)
