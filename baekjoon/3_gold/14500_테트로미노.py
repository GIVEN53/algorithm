from sys import stdin


def dfs(depth, total, r, c):
    global visited, res

    if res >= total + (4 - depth) * max_num:
        return

    if depth == 4:
        res = max(res, total)
        return

    for i in range(4):
        nr, nc = r + direction[i], c + direction[3 - i]
        if is_out_of_range(nr, nc) or visited[nr][nc]:
            continue
        if depth == 2:
            visited[nr][nc] = True
            dfs(depth + 1, total + board[nr][nc], r, c)
            visited[nr][nc] = False
        visited[nr][nc] = True
        dfs(depth + 1, total + board[nr][nc], nr, nc)
        visited[nr][nc] = False


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
direction = [1, 0, -1, 0]
res = 0
max_num = max(map(max, board))
for r in range(n):
    for c in range(m):
        visited[r][c] = True
        dfs(1, board[r][c], r, c)
        visited[r][c] = False

print(res)

##########################
#    memory: 38008KB     #
#    time:   176ms       #
##########################
