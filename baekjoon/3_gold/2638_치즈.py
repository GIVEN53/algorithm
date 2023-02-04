from collections import deque
from sys import stdin


def bfs_air(q: deque, cheese: list):
    global visited

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + row[i]
            ny = y + col[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue

            if board[nx][ny]:
                cheese.append((nx, ny))
            else:
                q.append((nx, ny))
            visited[nx][ny] = True

    return cheese


def get_melting_cheese(cheese):
    global board, visited

    melting_cheese = []
    for i, j in cheese:
        if is_melting_cheese(i, j):
            melting_cheese.append((i, j))
        else:
            visited[i][j] = False

    return melting_cheese


def is_melting_cheese(x, y):
    cnt = 0
    for i in range(4):
        nx = x + row[i]
        ny = y + col[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or not visited[nx][ny]:
            continue

        if not board[nx][ny]:
            cnt += 1

    return cnt >= 2


def melt(melting_cheese):
    global board

    for i, j in melting_cheese:
        board[i][j] = 0


n, m = map(int, stdin.readline().split())
board = [[*map(int, stdin.readline().split())] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

row = [0, 0, 1, -1]
col = [1, -1, 0, 0]
hours = 0

q = deque([(0, 0)])
while True:
    cheese = bfs_air(q, [])
    if not cheese:
        break

    melting_cheese = get_melting_cheese(cheese)
    melt(melting_cheese)
    q = deque(melting_cheese)
    hours += 1

print(hours)
