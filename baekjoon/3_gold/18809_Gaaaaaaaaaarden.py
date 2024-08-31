from sys import stdin
from itertools import combinations
from collections import deque


def bfs(garden, green, red):
    q = deque()
    time = [[0] * m for _ in range(n)]
    for r, c in green:
        garden[r][c] = 3  # green은 3으로 표기
        time[r][c] = 1
        q.append((r, c))
    for r, c in red:
        garden[r][c] = 4  # red는 4로 표기
        time[r][c] = 1
        q.append((r, c))

    flower_cnt = 0
    while q:
        r, c = q.popleft()
        if garden[r][c] == "F":  # 꽃이 피어난 땅은 배양액이 사라짐
            continue

        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if out_of_range(nr, nc) or not garden[nr][nc] or garden[nr][nc] == "F":
                continue  # 다음 땅이 범위를 벗어났거나 호수 또는 꽃이면 건너뜀

            if garden[nr][nc] == 1 or garden[nr][nc] == 2:  # 배양액이 퍼질 수 있는 땅
                time[nr][nc] = time[r][c] + 1
                garden[nr][nc] = garden[r][c]
                q.append((nr, nc))
            elif garden[r][c] != garden[nr][nc] and time[r][c] + 1 == time[nr][nc]:
                garden[nr][nc] = "F"  # 배양액이 다르고 동일한 시간이면 꽃이 핌
                flower_cnt += 1

    return flower_cnt


def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


n, m, g, r = map(int, stdin.readline().split())
garden = []
yellow_ground = []
for i in range(n):
    tmp = list(map(int, stdin.readline().split()))
    garden.append(tmp)
    for j in range(m):
        if tmp[j] == 2:
            yellow_ground.append((i, j))  # 배양액을 뿌릴 수 있는 황토색 칸

direction = [1, 0, -1, 0]
max_flower_cnt = 0
for comb in combinations(yellow_ground, g + r):  # 배양액을 뿌릴 칸 조합
    for green in combinations(comb, g):  # 초록색 배양액을 뿌릴 칸 조합
        red = tuple(x for x in comb if x not in green)  # 나머지는 빨간색 배양액
        garden_new = [row[:] for row in garden]  # 깊은 복사
        max_flower_cnt = max(max_flower_cnt, bfs(garden_new, green, red))  # 최댓값 갱신

print(max_flower_cnt)
