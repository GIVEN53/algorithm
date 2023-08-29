from sys import stdin
from collections import deque


def bfs(r, c, rain, q: deque):
    q.append((r, c))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc) or visited[nr][nc] or city[nr][nc] <= rain:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n


n = int(stdin.readline())
max_height = 0
city = []
for _ in range(n):
    c = list(map(int, stdin.readline().split()))
    max_height = max(max_height, max(c))
    city.append(c)

direction = [1, 0, -1, 0]
q = deque()
res = 0
for rain in range(max_height):
    visited = [[False] * n for _ in range(n)]
    area = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and city[r][c] > rain:
                visited[r][c] = True
                bfs(r, c, rain, q)
                area += 1
    res = max(res, area)

print(res)

##########################
#    memory: 34176KB     #
#    time:   948ms       #
##########################
