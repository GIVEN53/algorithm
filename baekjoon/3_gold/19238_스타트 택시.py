from sys import stdin
from collections import deque


def find_passenger(distances):
    for p in passengers:
        r, c = p[1:3]
        p[0] = distances[r - 1][c - 1]
    passengers.sort(reverse=True)
    return passengers.pop()


def bfs(start_r, start_c):
    visited = [[-1] * n for _ in range(n)]
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc) or visited[nr][nc] != -1:
                continue
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

    return visited


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n or board[r][c] == 1


n, m, fuel = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
tr, tc = map(int, stdin.readline().split())
passengers = []
for _ in range(m):
    passengers.append([0] + list(map(int, stdin.readline().split())))

direction = [1, 0, -1, 0]
for _ in range(m):
    distances = bfs(tr - 1, tc - 1)
    dist, sr, sc, dr, dc = find_passenger(distances)
    if dist == -1:
        fuel = -1
        break

    fuel -= dist
    if fuel <= 0:
        fuel = -1
        break

    distances = bfs(sr - 1, sc - 1)
    next_dist = distances[dr - 1][dc - 1]
    if next_dist == -1 or fuel < next_dist:
        fuel = -1
        break

    fuel += next_dist
    tr, tc = dr, dc

print(fuel)


##########################
#    memory: 34208KB     #
#    time:   440ms       #
##########################

### 고려 사항
# 1. 택시 시작점에 손님이 있는 경우 -> 거리 0
# 2. 택시 -> 승객 출발지로 갈 수 없는 경우 (출발지가 벽에 둘러 싸임) -> 거리 -1
# 3. 승객 출발지 -> 목적지로 갈 수 없는 경우 (목적지가 벽에 둘러 싸임) -> 거리 -1
# 4. 승객의 목적지가 모두 같을 수 있다 -> 2차원 list에 승객 저장 불가
# 5. A 승객의 목적지가 B 승객의 출발지일 수 있다 -> 2차원 list에 승객 저장 불가
