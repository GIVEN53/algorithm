# 1 2100ms
from sys import stdin
from collections import deque
from itertools import combinations


def bfs(comb):
    visited = [[0] * 5 for _ in range(5)]
    r, c = comb[0]  # 첫 번째 자리부터 시작
    q = deque([(r, c)])
    visited[r][c] = 1

    comb = set(comb)
    cnt = 1  # bfs로 찾은 자리 수
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if out_of_range(nr, nc) or (nr, nc) not in comb or visited[nr][nc]:
                continue

            cnt += 1
            visited[nr][nc] = 1
            q.append((nr, nc))

    if cnt == 7:  # 7자리 전부 찾으면 1 리턴
        return 1
    return 0


def out_of_range(r, c):
    return r < 0 or r > 4 or c < 0 or c > 4


seats = [list(stdin.readline().rstrip()) for _ in range(5)]
arr = []
for i in range(5):
    for j in range(5):
        arr.append((i, j))

res = 0
direction = [1, 0, -1, 0]
for comb in combinations(arr, 7):  # 25개 자리 중 7개 조합
    s_cnt = 0
    for r, c in comb:
        if seats[r][c] == "S":
            s_cnt += 1  # 이다솜파 수

    if s_cnt >= 4:  # 이다솜파 수가 4개 이상이면 bfs
        res += bfs(comb)

print(res)


# 2 52ms
from sys import stdin


def dfs(d, path, bit, y):
    global res

    if y > 3:  # 임도연파 수가 4개 이상이면 dfs 종료
        return

    if d == 7:  # 모두 탐색하면 경우의 수 증가
        res += 1
        return

    for r, c in path:  # 경로가 직선이 아니기 때문에 탐색한 경로 전부 순회
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if out_of_range(nr, nc):
                continue

            sub_bit = 1 << (5 * nr + nc)
            nbit = bit | sub_bit
            # 현재 dfs에서 탐색하지 않은 좌표거나 방문하지 않은 경로만 dfs
            if not bit & sub_bit and nbit not in visited:
                visited.add(nbit)
                dfs(d + 1, path + [(nr, nc)], nbit, y + 1 if seat[nr][nc] == "Y" else y)


def out_of_range(r, c):
    return r < 0 or r > 4 or c < 0 or c > 4


seat = [list(stdin.readline().rstrip()) for _ in range(5)]

res = 0
visited = set()
direction = [1, 0, -1, 0]
for i in range(5):
    for j in range(5):
        if seat[i][j] == "S":
            dfs(1, [(i, j)], 1 << (5 * i + j), 0)

print(res)
