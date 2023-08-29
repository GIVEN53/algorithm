from sys import stdin
from collections import deque


def move_cloud(move_r, move_c) -> set:
    moved_cloud = set()
    while cloud:
        r, c = cloud.popleft()

        r, c = (r + move_r) % n, (c + move_c) % n
        board[r][c] += 1
        moved_cloud.add((r, c))
    return moved_cloud


def copy_diagonal(moved_cloud: set):
    for r, c in moved_cloud:
        cnt = 0
        for d in range(1, 8, 2):
            nr, nc = r + direction[d][0], c + direction[d][1]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc]:
                cnt += 1
        board[r][c] += cnt


def create_cloud(moved_cloud: set):
    for i in range(n):
        for j in range(n):
            if board[i][j] < 2 or (i, j) in moved_cloud:
                continue
            cloud.append((i, j))
            board[i][j] -= 2


n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

cloud = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])
direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
for _ in range(m):
    d, s = map(int, stdin.readline().split())
    move_r, move_c = direction[d - 1][0] * s, direction[d - 1][1] * s
    moved_cloud = move_cloud(move_r, move_c)
    copy_diagonal(moved_cloud)
    create_cloud(moved_cloud)

print(sum(sum(b) for b in board))

##########################
#    memory: 34232KB     #
#    time:   256ms       #
##########################
