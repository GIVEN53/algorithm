# 1 dfs 시간 초과
from sys import stdin


def spread_fire(prev):
    cnt = 0
    for f in range(prev, len(fire)):
        r, c = fire[f]
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc) or is_not_space(nr, nc):
                continue
            maze[nr][nc] = "F"
            fire.append((nr, nc))
            cnt += 1
    return len(fire) - cnt


def rollback_fire(now):
    while fire and len(fire) > now:
        r, c = fire[-1]
        maze[r][c] = "."
        fire.pop()


def backtracking(r, c, minutes, prev_fire):
    global ans

    edge_dist = min(r - 0, R - 1 - r, c - 0, C - 1 - c)
    if edge_dist == 0:
        ans = min(ans, minutes + 1)
        return
    if edge_dist + minutes + 1 > ans:
        return

    now_fire = spread_fire(prev_fire)
    for i in range(4):
        nr, nc = r + direction[i], c + direction[3 - i]
        if is_not_space(nr, nc) or visited[nr][nc]:
            continue
        visited[nr][nc] = True
        backtracking(nr, nc, minutes + 1, now_fire)
        visited[nr][nc] = False
    rollback_fire(now_fire)


def is_not_space(r, c):
    return maze[r][c] == "#" or maze[r][c] == "F"


def is_out_of_range(r, c):
    return r < 0 or r >= R or c < 0 or c >= C


R, C = map(int, stdin.readline().split())
maze = []
jihoon: tuple
fire = []
for r in range(R):
    m = list(stdin.readline().rstrip())
    for c in range(C):
        if m[c] == "J":
            jihoon = (r, c)
        elif m[c] == "F":
            fire.append((r, c))
    maze.append(m)

visited = [[False] * C for _ in range(R)]
visited[jihoon[0]][jihoon[1]] = True
direction = [1, 0, -1, 0]
ans = 1e9
backtracking(*jihoon, 0, 0)
print(ans if ans != 1e9 else "IMPOSSIBLE")


# 2 bfs
from sys import stdin
from collections import deque


def escape():
    global ans

    maze[jihoon[0][0]][jihoon[0][1]] = -1
    minutes = 0
    while jihoon:
        minutes += 1
        spread_fire()
        for _ in range(len(jihoon)):
            r, c = jihoon.popleft()
            for i in range(4):
                nr, nc = r + direction[i], c + direction[3 - i]
                if is_out_of_range(nr, nc):
                    ans = min(ans, minutes)
                    continue
                if is_not_space(nr, nc) or maze[nr][nc] == -1:
                    continue
                maze[nr][nc] = -1
                jihoon.append((nr, nc))


def spread_fire():
    for _ in range(len(fire)):
        r, c = fire.popleft()
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc) or is_not_space(nr, nc):
                continue
            maze[nr][nc] = "F"
            fire.append((nr, nc))


def is_not_space(r, c):
    return maze[r][c] == "#" or maze[r][c] == "F"


def is_out_of_range(r, c):
    return r < 0 or r >= R or c < 0 or c >= C


R, C = map(int, stdin.readline().split())
maze = []
jihoon = deque()
fire = deque()
for r in range(R):
    m = list(stdin.readline().rstrip())
    for c in range(C):
        if m[c] == "F":
            fire.append((r, c))
        elif m[c] == "J":
            jihoon.append((r, c))
    maze.append(m)

direction = [1, 0, -1, 0]
ans = 1e9
escape()
print(ans if ans != 1e9 else "IMPOSSIBLE")

##########################
#    memory: 39440KB     #
#    time:   1772ms      #
##########################
