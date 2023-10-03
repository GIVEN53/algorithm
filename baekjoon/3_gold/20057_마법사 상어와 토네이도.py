from sys import stdin
from math import floor


def tornado(r, c, d):
    over_amount = 0
    sand, board[r][c] = board[r][c], 0
    dr, dc = direction[d]
    tmp = 0
    for i in range(9):
        pr, pc = p_direction[d][i]
        moved_sand = floor(sand * percent[i])
        if is_out_of_range(r + pr, c + pc):
            over_amount += moved_sand
        else:
            board[r + pr][c + pc] += moved_sand
        tmp += moved_sand

    sand -= tmp
    if is_out_of_range(r + dr, c + dc):
        over_amount += sand
    else:
        board[r + dr][c + dc] += sand

    return over_amount


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n


n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
percent = [0.01, 0.07, 0.02, 0.1, 0.05, 0.1, 0.07, 0.02, 0.01]
p_direction = [
    [(-1, 1), (-1, 0), (-2, 0), (-1, -1), (0, -2), (1, -1), (1, 0), (2, 0), (1, 1)],
    [(-1, -1), (0, -1), (0, -2), (1, -1), (2, 0), (1, 1), (0, 1), (0, 2), (-1, 1)],
    [(1, -1), (1, 0), (2, 0), (1, 1), (0, 2), (-1, 1), (-1, 0), (-2, 0), (-1, -1)],
    [(1, 1), (0, 1), (0, 2), (-1, 1), (-2, 0), (-1, -1), (0, -1), (0, -2), (1, -1)],
]
moved = [0] * n
d, cnt = 0, 1
r = c = n // 2
res = 0
while r != 0 or c != 0:
    if moved[cnt] == 2 and cnt < n - 1:
        cnt += 1

    for _ in range(cnt):
        r += direction[d][0]
        c += direction[d][1]
        res += tornado(r, c, d)

    d = (d + 1) % 4
    moved[cnt] += 1

print(res)


##########################
#    memory: 43568KB     #
#    time:   1148ms      #
##########################
