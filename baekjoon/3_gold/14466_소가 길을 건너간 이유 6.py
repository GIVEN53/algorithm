from collections import deque
from sys import stdin


def bfs(q: deque):
    global visited_farm

    pair_cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + direction[i], y + direction[3 - i]
            if is_out_of_range(nx, ny) or is_road(x, y, nx, ny):
                continue

            if not visited_farm[nx][ny]:
                if (nx, ny) in cow:
                    pair_cnt += 1
                visited_farm[nx][ny] = True
                q.append((nx, ny))

    return K - pair_cnt


def is_out_of_range(x, y):
    return x < 0 or x > N - 1 or y < 0 or y > N - 1


def is_road(x, y, nx, ny):
    return (nx, ny) in road[x][y]


N, K, R = map(int, stdin.readline().split())
road = [[set() for _ in range(N)] for _ in range(N)]
for _ in range(R):
    r, c, nr, nc = map(int, stdin.readline().split())
    road[r - 1][c - 1].add((nr - 1, nc - 1))
    road[nr - 1][nc - 1].add((r - 1, c - 1))
    
cow = set()
for _ in range(K):
    r, c = map(int, stdin.readline().split())
    cow.add((r - 1, c - 1))

direction = (-1, 0, 1, 0)
not_pair_cnt = 0
q = deque()
for x, y in cow:
    visited_farm = [[False] * N for _ in range(N)]
    visited_farm[x][y] = True
    q.append((x, y))
    not_pair_cnt += bfs(q)

print(not_pair_cnt // 2)
