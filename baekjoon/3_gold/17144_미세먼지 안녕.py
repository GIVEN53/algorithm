import copy
from sys import stdin


def is_cleaner(r, c):
    return dusts[r][c] == -1


def is_out_of_range(r, c):
    return r < 0 or r > R - 1 or c < 0 or c > C - 1


def diffuse():
    temp_dusts = copy.deepcopy(dusts)

    for i in range(R):
        for j in range(C):
            if is_cleaner(i, j):
                continue

            amount = dusts[i][j] // 5
            for k in range(4):
                new_r = i + row[k]
                new_c = j + col[k]
                if is_out_of_range(new_r, new_c) or is_cleaner(new_r, new_c):
                    continue

                temp_dusts[i][j] += dusts[new_r][new_c] // 5
                temp_dusts[i][j] -= amount

    return temp_dusts


def move(r, c, clock_wise):
    if clock_wise:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        limit_r = cleaner_r - 1
    else:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        limit_r = cleaner_r

    i = 0
    while i < 4:
        next_r, next_c = r + directions[i][0], c + directions[i][1]

        if is_out_of_range(next_r, next_c) or next_r == limit_r:
            i += 1
            continue

        if is_cleaner(next_r, next_c):
            i += 1
            dusts[r][c] = 0
            continue

        dusts[r][c] = dusts[next_r][next_c]
        r = next_r
        c = next_c


R, C, T = map(int, stdin.readline().split())

dusts = [0] * R
cleaner_r = 0
for i in range(R):
    d = list(map(int, stdin.readline().split()))
    dusts[i] = d
    if d[0] == -1:
        cleaner_r = i

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
for _ in range(T):
    dusts = diffuse()
    move(cleaner_r - 2, 0, False)
    move(cleaner_r + 1, 0, True)

print(sum(sum(i) for i in dusts) + 2)
