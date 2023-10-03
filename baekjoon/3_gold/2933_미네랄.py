from sys import stdin
from collections import deque


def destroy_mineral(h):
    global left

    if left:
        left = 0
        for i in range(C):
            if cave[h][i] == "x":
                cave[h][i] = "."
                return h, i
    elif not left:
        left = 1
        for i in range(C - 1, -1, -1):
            if cave[h][i] == "x":
                cave[h][i] = "."
                return h, i
    return -1, -1


def find_cluster(start_r, start_c):
    cluster = [[0] * C for _ in range(R)]
    cluster[start_r][start_c] = 1
    q = deque([(start_r, start_c)])

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range_or_not_mineral(nr, nc) or cluster[nr][nc]:
                continue
            cluster[nr][nc] = 1
            q.append((nr, nc))

    return cluster


def get_max_rows(cluster):
    max_rows = [-1] * C
    for c in range(C):
        for r in range(R - 1, -1, -1):
            if cluster[r][c]:
                max_rows[c] = r
                break

    return max_rows


def get_fall_height(max_rows):
    min_height = 100
    for c, row in enumerate(max_rows):
        if row == -1:
            continue

        for r in range(row + 1, R):
            if cave[r][c] == "x":
                min_height = min(min_height, r - row - 1)
                break
            if r == R - 1:
                min_height = min(min_height, r - row)

    return min_height


def is_out_of_range_or_not_mineral(r, c):
    return r < 0 or r >= R or c < 0 or c >= C or cave[r][c] == "."


R, C = map(int, stdin.readline().split())
cave = [list(stdin.readline().rstrip()) for _ in range(R)]
_ = int(stdin.readline())
heights = [*map(int, stdin.readline().split())]

direction = [1, 0, -1, 0]
left = 1
for height in heights:
    mr, mc = destroy_mineral(R - height)
    if mr == mc == -1:
        continue

    for i in range(4):
        nr, nc = mr + direction[i], mc + direction[3 - i]
        if is_out_of_range_or_not_mineral(nr, nc):
            continue

        cluster = find_cluster(nr, nc)
        max_rows = get_max_rows(cluster)
        if R - 1 in max_rows:
            continue

        h = get_fall_height(max_rows)
        for r in range(R - 1, -1, -1):
            for c in range(C):
                if cluster[r][c]:
                    cave[r][c] = "."
                    cave[r + h][c] = "x"
        break

for row in cave:
    print("".join(row))


##########################
#    memory: 34296KB     #
#    time:   1308ms      #
##########################
