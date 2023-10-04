from sys import stdin


def up(board):
    r_idx = [0] * n
    for r in range(1, n):
        for c in range(n):
            if board[r][c] == 0:
                continue

            if board[r_idx[c]][c] == 0:
                board[r_idx[c]][c] += board[r][c]
                board[r][c] = 0
            elif board[r_idx[c]][c] == board[r][c]:
                board[r_idx[c]][c] += board[r][c]
                board[r][c] = 0
                r_idx[c] += 1
            else:
                r_idx[c] += 1
                if r == r_idx[c]:
                    continue
                board[r_idx[c]][c] += board[r][c]
                board[r][c] = 0
    return board


def down(board):
    r_idx = [n - 1] * n
    for r in range(n - 2, -1, -1):
        for c in range(n):
            if board[r][c] == 0:
                continue

            if board[r_idx[c]][c] == 0:
                board[r_idx[c]][c] += board[r][c]
                board[r][c] = 0
            elif board[r_idx[c]][c] == board[r][c]:
                board[r_idx[c]][c] += board[r][c]
                board[r][c] = 0
                r_idx[c] -= 1
            else:
                r_idx[c] -= 1
                if r == r_idx[c]:
                    continue
                board[r_idx[c]][c] += board[r][c]
                board[r][c] = 0
    return board


def left(board):
    c_idx = [0] * n
    for c in range(1, n):
        for r in range(n):
            if board[r][c] == 0:
                continue

            if board[r][c_idx[r]] == 0:
                board[r][c_idx[r]] += board[r][c]
                board[r][c] = 0
            elif board[r][c_idx[r]] == board[r][c]:
                board[r][c_idx[r]] += board[r][c]
                board[r][c] = 0
                c_idx[r] += 1
            else:
                c_idx[r] += 1
                if c == c_idx[r]:
                    continue
                board[r][c_idx[r]] += board[r][c]
                board[r][c] = 0
    return board


def right(board):
    c_idx = [n - 1] * n
    for c in range(n - 2, -1, -1):
        for r in range(n):
            if board[r][c] == 0:
                continue

            if board[r][c_idx[r]] == 0:
                board[r][c_idx[r]] += board[r][c]
                board[r][c] = 0
            elif board[r][c_idx[r]] == board[r][c]:
                board[r][c_idx[r]] += board[r][c]
                board[r][c] = 0
                c_idx[r] -= 1
            else:
                c_idx[r] -= 1
                if c == c_idx[r]:
                    continue
                board[r][c_idx[r]] += board[r][c]
                board[r][c] = 0
    return board


# 1 (396ms)
def start_game(direction):
    global ans

    tmp = [b[:] for b in board]
    for i in direction:
        if i == 0:
            tmp = up(tmp)
        elif i == 1:
            tmp = down(tmp)
        elif i == 2:
            tmp = left(tmp)
        else:
            tmp = right(tmp)
    ans = max(ans, max(map(max, tmp)))


def dfs(direction: list):
    if len(direction) == 5:
        start_game(direction)
        return

    for i in range(4):
        direction.append(i)
        dfs(direction)
        direction.pop()


n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
ans = 0
for i in range(4):
    dfs([i])
print(ans)


# 2 (388ms)
from itertools import product

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
ans = 0
for direction in product([0, 1, 2, 3], repeat=5):
    tmp = [b[:] for b in board]
    for i in direction:
        if i == 0:
            tmp = up(tmp)
        elif i == 1:
            tmp = down(tmp)
        elif i == 2:
            tmp = left(tmp)
        else:
            tmp = right(tmp)
    ans = max(ans, max(map(max, tmp)))
print(ans)


##########################
#    memory: 31256KB     #
#    time:   388ms      #
##########################
