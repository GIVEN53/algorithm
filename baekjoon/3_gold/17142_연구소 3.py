from sys import stdin
from collections import deque
from itertools import combinations


def bfs(virus, empty_cnt) -> int:
    q = deque(virus)
    visited = [[0] * n for _ in range(n)]
    for r, c in virus:
        visited[r][c] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc):
                continue

            if not visited[nr][nc]:
                if lab[nr][nc] == 0:
                    empty_cnt -= 1
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

            if empty_cnt == 0:
                return visited[r][c]

    return n**2


def is_out_of_range(r, c):
    return 0 > r or r >= n or 0 > c or c >= n or lab[r][c] == 1


n, m = map(int, stdin.readline().split())
lab = []
virus = []
empty_cnt = 0
for i in range(n):
    line = list(map(int, stdin.readline().split()))
    lab.append(line)
    for j in range(n):
        if line[j] == 0:
            empty_cnt += 1
        elif line[j] == 2:
            virus.append((i, j))
if empty_cnt == 0:
    print(0)
    exit()

direction = [1, 0, -1, 0]
min_sec = n**2
for comb in combinations(virus, m):
    min_sec = min(min_sec, bfs(comb, empty_cnt))

if min_sec == n**2:
    print(-1)
else:
    print(min_sec)

##########################
#    memory: 34208KB     #
#    time:   652ms       #
##########################
