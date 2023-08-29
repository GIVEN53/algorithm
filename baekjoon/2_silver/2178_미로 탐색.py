from sys import stdin
from collections import deque


def bfs(x, y):
    q = deque([(x, y, maze[x][y])])

    while q:
        r, c, cnt = q.popleft()

        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc):
                continue
            if maze[nr][nc] == 0 or maze[nr][nc] > cnt + 1:
                maze[nr][nc] = cnt + 1
                q.append((nr, nc, cnt + 1))


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m or arr[r][c] == "0"


n, m = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(n)]

maze = [[0] * m for _ in range(n)]
maze[n - 1][m - 1] = 1
direction = [1, 0, -1, 0]
bfs(n - 1, m - 1)

print(maze[0][0])

##########################
#    memory: 34176KB     #
#    time:   84ms        #
##########################
