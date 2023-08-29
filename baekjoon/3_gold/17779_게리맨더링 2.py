from sys import stdin


def get_wards(r, c, d1, d2) -> list:
    wards = [0] * 5
    boundary = draw_boundary(r, c, d1, d2)

    wards[0] = sum_ward(boundary, 0, r + d1, 0, c + 1, 1, 1)
    wards[1] = sum_ward(boundary, 0, r + d2 + 1, n - 1, c, 1, -1)
    wards[2] = sum_ward(boundary, n - 1, r + d1 - 1, 0, c - d1 + d2, -1, 1)
    wards[3] = sum_ward(boundary, n - 1, r + d2, n - 1, c - d1 + d2 - 1, -1, -1)
    return wards


def draw_boundary(r, c, d1, d2) -> list:
    boundary = [[0] * n for _ in range(n)]

    for i in range(d1 + 1):
        boundary[r + i][c - i] = 1
        boundary[r + i + d2][c - i + d2] = 1
    for i in range(d2 + 1):
        boundary[r + i][c + i] = 1
        boundary[r + i + d1][c + i - d1] = 1

    return boundary


def sum_ward(boundary, r_start, r_end, c_start, c_end, k, j) -> int:
    total = 0
    for r in range(r_start, r_end, k):
        for c in range(c_start, c_end, j):
            if boundary[r][c]:
                break
            total += city[r][c]
    return total


n = int(stdin.readline())

city = []
total_population = 0
for _ in range(n):
    c = list(map(int, stdin.readline().split()))
    total_population += sum(c)
    city.append(c)

res = 1e9
for r in range(n - 2):
    for c in range(1, n - 1):
        for d1 in range(1, n):
            if c - d1 < 0:
                continue
            for d2 in range(1, n):
                if r + d1 + d2 > n - 1 or c + d2 > n - 1:
                    continue
                wards = get_wards(r, c, d1, d2)
                wards[4] = total_population - sum(wards)
                res = min(res, max(wards) - min(wards))

print(res)

##########################
#    memory: 31256KB     #
#    time:   476ms       #
##########################
