from sys import stdin
from collections import deque


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n


def turn_direction(moving, i):
    if moving == "L":
        return (i + 3) % 4
    else:
        return (i + 1) % 4


n, k = int(stdin.readline()), int(stdin.readline())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, stdin.readline().split())
    board[r - 1][c - 1] = 1

L = int(stdin.readline())
moves = deque(stdin.readline().split() for _ in range(L))

r = c = 0
snake = deque([(r, c)])
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 1
second = 0
while True:
    second += 1
    r, c = r + direction[d][0], c + direction[d][1]
    if is_out_of_range(r, c) or (r, c) in snake:
        break

    snake.append((r, c))
    if board[r][c] == 1:
        board[r][c] = 0
    else:
        snake.popleft()

    if moves and second == int(moves[0][0]):
        d = turn_direction(moves[0][1], d)
        moves.popleft()

print(second)

##########################
#    memory: 34200KB     #
#    time:   68ms        #
##########################
