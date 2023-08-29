from sys import stdin


def dfs(r, c, now_cnt):
    global max_cnt

    if alphabet[board[r][c]]:
        max_cnt = max(max_cnt, now_cnt)
        return

    alphabet[board[r][c]] = True
    for i in range(4):
        nr, nc = r + direction[i], c + direction[3 - i]
        if 0 <= nr < R and 0 <= nc < C:
            dfs(nr, nc, now_cnt + 1)
    alphabet[board[r][c]] = False


R, C = map(int, stdin.readline().split())
board = [list(map(lambda x: ord(x) - 65, stdin.readline().rstrip())) for _ in range(R)]

alphabet = [False] * 26
direction = [1, 0, -1, 0]
max_cnt = 0
dfs(0, 0, 0)

print(max_cnt)

##########################
#    PyPy3               #
#    memory: 166452KB    #
#    time:   5720ms      #
##########################
