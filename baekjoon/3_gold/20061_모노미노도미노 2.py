from sys import stdin
from collections import deque


def find_top(board, c):
    for r in range(2, 6):
        if board[r][c] == 1:
            return r - 1
    return 5


def remove_full_col():
    global res
    for board in blue, green:
        for r in range(2, 6):
            if sum(board[r]) == 4:
                del board[r]
                board.appendleft([0] * 4)
                res += 1


def execute_special():
    for board in blue, green:
        while 1 in board[1]:
            board.pop()
            board.appendleft([0] * 4)


blue = deque([deque([0] * 4) for _ in range(6)])
green = deque([deque([0] * 4) for _ in range(6)])

n = int(stdin.readline())
res = 0
for _ in range(n):
    t, r, c = map(int, stdin.readline().split())
    br, gr = find_top(blue, r), find_top(green, c)
    if t == 2:
        gr = min(gr, find_top(green, c + 1))
        blue[br - 1][r], green[gr][c + 1] = 1, 1
    elif t == 3:
        br = min(br, find_top(blue, r + 1))
        blue[br][r + 1], green[gr - 1][c] = 1, 1
    blue[br][r], green[gr][c] = 1, 1
    remove_full_col()
    execute_special()

print(res)
print(sum(map(sum, blue)) + sum(map(sum, green)))

##########################
#    memory: 34332KB     #
#    time:   112ms       #
##########################
