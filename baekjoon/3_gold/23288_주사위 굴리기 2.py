from sys import stdin
from collections import deque


def bfs(r, c) -> set:
    q = deque([(r, c)])
    same_scores = {(r, c)}
    while q:
        r, c = q.popleft()
        for d in direction:
            nr, nc = r + d[0], c + d[1]
            if is_out_of_range(nr, nc) or (nr, nc) in same_scores:
                continue
            if board[nr][nc] == board[r][c]:
                q.append((nr, nc))
                same_scores.add((nr, nc))

    return same_scores


def roll(dice, d) -> list:
    top, north, east, west, south, bottom = dice
    if d == 0:
        return [south, top, east, west, bottom, north]
    elif d == 1:
        return [west, north, top, bottom, south, east]
    elif d == 2:
        return [north, bottom, east, west, top, south]
    else:
        return [east, north, bottom, top, south, west]


def move(r, c, d):
    nr, nc = r + direction[d][0], c + direction[d][1]
    if is_out_of_range(nr, nc):
        d = (d + 2) % 4
    r += direction[d][0]
    c += direction[d][1]

    return r, c, d


def is_out_of_range(r, c) -> bool:
    return r < 0 or r >= n or c < 0 or c >= m


def rotate_direction(bottom, space, d) -> int:
    if bottom > space:
        d = (d + 1) % 4
    elif bottom < space:
        d = (d - 1) % 4

    return d


n, m, k = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

scores = [[0] * m for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for r in range(n):
    for c in range(m):
        if scores[r][c] == 0:
            same_scores = bfs(r, c)
            score = len(same_scores) * board[r][c]
            for sr, sc in same_scores:
                scores[sr][sc] = score

dice = [1, 2, 3, 4, 5, 6]
r, c, d = 0, 0, 1
result = 0
while k:
    r, c, d = move(r, c, d)
    dice = roll(dice, d)
    result += scores[r][c]
    d = rotate_direction(dice[-1], board[r][c], d)
    k -= 1

print(result)

##########################
#    memory: 34436KB     #
#    time:   76ms        #
##########################
