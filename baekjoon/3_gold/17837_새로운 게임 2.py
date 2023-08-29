from sys import stdin


def move():
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    turn_cnt = 1
    while turn_cnt < 1001:
        for i in range(k):
            r, c, d = pieces[i]
            nr, nc = r + direction[d][0], c + direction[d][1]
            if is_out_of_range(nr, nc) or color[nr][nc] == "2":
                d = d + 1 if d % 2 == 0 else d - 1
                nr, nc = r + direction[d][0], c + direction[d][1]
                pieces[i][2] = d
                if is_out_of_range(nr, nc) or color[nr][nc] == "2":
                    continue

            tmp = []
            while board[r][c][-1] != i:
                tmp.append(board[r][c].pop())
            tmp.append(board[r][c].pop())

            if color[nr][nc] == "0":
                tmp.reverse()

            board[nr][nc].extend(tmp)
            for j in tmp:
                pieces[j][0], pieces[j][1] = nr, nc

            if len(board[nr][nc]) >= 4:
                return turn_cnt
        turn_cnt += 1

    return -1


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n


n, k = map(int, stdin.readline().split())
color = [stdin.readline().split() for _ in range(n)]
board = [[[] for _ in range(n)] for _ in range(n)]
pieces = [None] * k
for i in range(k):
    r, c, d = map(int, stdin.readline().split())
    pieces[i] = [r - 1, c - 1, d - 1]
    board[r - 1][c - 1].append(i)

print(move())

##########################
#    memory: 31256KB     #
#    time:   52ms        #
##########################
