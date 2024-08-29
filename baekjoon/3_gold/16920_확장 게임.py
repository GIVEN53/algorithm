from sys import stdin
from collections import deque


def bfs(player):
    global expanded

    q = castle[player]
    for _ in range(s[player]):  # 이동 가능한 칸 수만큼 이동
        if not q:  # 큐가 비어있으면 탈출
            break
        for _ in range(len(q)):  # 이동 가능한 레벨이 같은 좌표만 순회
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + direction[i], c + direction[3 - i]
                if out_of_range(nr, nc) or not empty[nr][nc]:
                    continue  # 다음 칸이 범위를 벗어났거나 비어있지 않은 칸이면 건너뜀

                castle_cnt[player] += 1  # 성칸 개수 추가
                empty[nr][nc] = 0  # 비어있지 않은 칸으로 변경
                q.append((nr, nc))
                expanded = True  # 확장했으면 확장 여부 체크

    return expanded


def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


n, m, p = map(int, stdin.readline().split())
s = list(map(int, stdin.readline().split()))

castle = [deque() for _ in range(p)]
castle_cnt = [0] * p
empty = [[0] * m for _ in range(n)]
for i in range(n):
    g = list(stdin.readline().rstrip())
    for j in range(len(g)):
        if g[j] != "." and g[j] != "#":
            castle[int(g[j]) - 1].append((i, j))  # 성 칸 좌표
            castle_cnt[int(g[j]) - 1] += 1  # 성 칸 개수
        if g[j] == ".":
            empty[i][j] = 1  # 빈 칸

direction = [1, 0, -1, 0]
expanded = True  # 확장 여부
while expanded:  # 모든 플레이어의 성이 확장되지 않았으면 while문 탈출
    expanded = False
    for player in range(p):  # 플레이어마다 성 확장
        expanded = bfs(player)

print(*castle_cnt)

""" 반례1
4 10 4
1000000000 1 100 99999
1#........
#.........
2#.......#
3#......#4

벽에 막혀서 확장 불가
"""

""" 반례2
2 8 1
1000000000
.#......
#......1

빈 칸에 접근 불가
"""
