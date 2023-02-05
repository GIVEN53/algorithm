from heapq import heappop, heappush
from sys import stdin


# bfs
def bfs():
    global dp

    q = []
    heappush(q, (-board[0][0], 0, 0))
    while q:
        _, x, y = heappop(q)

        for i in range(4):
            nx = x + row[i]
            ny = y + col[i]
            if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1:
                continue

            if board[x][y] > board[nx][ny]:
                if not dp[nx][ny]:
                    heappush(q, (-board[nx][ny], nx, ny))
                dp[nx][ny] += dp[x][y]

    return dp[m - 1][n - 1]


m, n = map(int, stdin.readline().split())
board = [[*map(int, stdin.readline().split())] for _ in range(m)]

row = [0, 0, 1, -1]
col = [1, -1, 0, 0]
dp, dp[0][0] = [[0] * n for _ in range(m)], 1
print(bfs())


# dfs
def dfs(x, y):
    global dp

    if x == m - 1 and y == n - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + row[i]
        ny = y + col[i]
        if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1:
            continue

        if board[x][y] > board[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


m, n = map(int, stdin.readline().split())
board = [[*map(int, stdin.readline().split())] for _ in range(m)]

row = [0, 0, 1, -1]
col = [1, -1, 0, 0]
dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))
