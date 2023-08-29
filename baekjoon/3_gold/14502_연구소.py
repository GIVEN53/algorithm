from sys import stdin
from itertools import combinations
from collections import deque


def spread(new_wall):
    tmp_lab = [i[:] for i in lab]
    for r, c in new_wall:
        tmp_lab[r][c] = 1
    q = deque(virus)

    infection = 0
    while q:
        r, c = q.popleft()
        infection += 1

        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]

            if 0 <= nr < n and 0 <= nc < m and tmp_lab[nr][nc] == 0:
                tmp_lab[nr][nc] = 2
                q.append((nr, nc))

    return not_wall - infection


n, m = map(int, stdin.readline().split())
lab = [list(map(int, stdin.readline().split())) for _ in range(n)]

empty_space = []
virus = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty_space.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

direction = [1, 0, -1, 0]
not_wall = len(empty_space) + len(virus) - 3
res = 0
for new_wall in combinations(empty_space, 3):
    empty_cnt = spread(new_wall)
    res = max(res, empty_cnt)

print(res)

##########################
#    memory: 34332KB     #
#    time:   1740ms      #
##########################
