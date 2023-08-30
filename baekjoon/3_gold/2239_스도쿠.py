from sys import stdin


def is_possible(r, c, v):
    return not (row[r][v] or col[c][v] or sub_square[r // 3 * 3 + c // 3][v])


def update(r, c, v, is_existed):
    row[r][v] = col[c][v] = sub_square[r // 3 * 3 + c // 3][v] = is_existed


def back_tracking(n):
    if n == len(blank):
        for s in sudoku:
            print(*s, sep="")
        exit()

    r, c = blank[n]
    for v in range(1, 10):
        if is_possible(r, c, v):
            update(r, c, v, True)
            sudoku[r][c] = v
            back_tracking(n + 1)
            update(r, c, v, False)
            sudoku[r][c] = 0


row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
sub_square = [[False] * 10 for _ in range(9)]

sudoku = []
blank = []
for i in range(9):
    s = list(map(int, stdin.readline().rstrip()))
    for j in range(9):
        v = s[j]
        if v == 0:
            blank.append((i, j))
            continue
        row[i][v] = True
        col[j][v] = True
        sub_square[i // 3 * 3 + j // 3][v] = True
    sudoku.append(s)

back_tracking(0)

##########################
#    memory: 31256KB     #
#    time:   5368ms      #
##########################
