from sys import stdin
from collections import deque


def bfs(q: deque):
    visited = [[False] * n for _ in range(n)]
    visited[shark_r][shark_c] = True

    eatable_fish = []
    min_dist = 1e9
    while q:
        dist, r, c = q.popleft()
        if dist > min_dist:
            continue

        dist += 1
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc) or visited[nr][nc]:
                continue

            visited[nr][nc] = True
            fish = sea[nr][nc]
            if 0 < fish < shark_size:
                eatable_fish.append((dist, nr, nc))
                min_dist = min(dist, min_dist)
            elif not fish or fish == shark_size:
                q.append((dist, nr, nc))

    if eatable_fish:
        eatable_fish.sort()
        return eatable_fish[0]

    return (0, 0, 0)


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n


n = int(stdin.readline())
sea = []
for i in range(n):
    fishes = list(map(int, stdin.readline().split()))
    for j in range(n):
        if fishes[j] == 9:
            shark_r, shark_c = i, j
            fishes[j] = 0
    sea.append(fishes)

sec, eat_cnt, shark_size = 0, 0, 2
direction = [1, 0, -1, 0]
q = deque()
while True:
    q.append((0, shark_r, shark_c))
    dist, shark_r, shark_c = bfs(q)
    if not dist:
        break

    sea[shark_r][shark_c] = 0
    sec += dist
    eat_cnt += 1
    if shark_size == eat_cnt:
        shark_size += 1
        eat_cnt = 0

print(sec)

##########################
#    memory: 34232KB     #
#    time:   68ms        #
##########################
