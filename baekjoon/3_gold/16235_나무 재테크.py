from sys import stdin
from collections import deque


def spring_summer_winter():
    for r in range(n):
        for c in range(n):
            dead_tree = 0
            for _ in range(len(tree[r][c])):
                age = tree[r][c].popleft()

                if nutrient[r][c] >= age:
                    nutrient[r][c] -= age
                    tree[r][c].append(age + 1)
                else:
                    dead_tree += age // 2
            nutrient[r][c] += dead_tree
            nutrient[r][c] += A[r][c]


def fall():
    tmp = []
    for r in range(n):
        for c in range(n):
            for q in range(len(tree[r][c])):
                if tree[r][c][q] % 5 == 0:
                    for dr, dc in direction:
                        nr, nc = r + dr, c + dc
                        if is_out_of_range(nr, nc):
                            continue

                        tmp.append((nr, nc))
    for r, c in tmp:
        tree[r][c].appendleft(1)


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n


n, m, k = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, age = map(int, stdin.readline().split())
    tree[r - 1][c - 1].append(age)

nutrient = [[5] * n for _ in range(n)]
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for _ in range(k):
    spring_summer_winter()
    fall()

cnt = 0
for r in range(n):
    for c in range(n):
        cnt += len(tree[r][c])

print(cnt)

##########################
#    memory: 220632KB    #
#    time:   964ms       #
##########################
