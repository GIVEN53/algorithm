from sys import stdin
from collections import deque


def bfs(r, c):
    q = deque([(r, c)])
    opened = [(r, c)]
    tot = country[r][c]
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc) or visited[nr][nc] == day:
                continue

            if is_within_population(r, c, nr, nc):
                visited[nr][nc] = day
                tot += country[nr][nc]
                q.append((nr, nc))
                opened.append((nr, nc))

    if len(opened) > 1:
        move(opened, tot)


def is_out_of_range(r, c):
    return r < 0 or r >= N or c < 0 or c >= N


def is_within_population(r, c, nr, nc):
    return L <= abs(country[r][c] - country[nr][nc]) <= R


def move(opened, tot):
    avg = tot // len(opened)
    for r, c in opened:
        country[r][c] = avg
        candidate.append((r, c))


N, L, R = map(int, stdin.readline().split())
country = [list(map(int, stdin.readline().split())) for _ in range(N)]

candidate = deque([(i, j) for i in range(N) for j in range(i % 2, N, 2)])
visited = [[-1] * N for _ in range(N)]
direction = [1, 0, -1, 0]
day = 0
while candidate:
    for _ in range(len(candidate)):
        r, c = candidate.popleft()
        if visited[r][c] == day:
            continue
        visited[r][c] = day
        bfs(r, c)

    day += 1

print(day - 1)

##########################
#    memory: 34240KB     #
#    time:   312ms       #
##########################
