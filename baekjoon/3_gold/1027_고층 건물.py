# sol 1
from sys import stdin


def find_left(start):
    if start - 2 < 0:
        return
    tmp = (start - 1, building[start - 1])
    for left in range(start - 2, -1, -1):
        y = get_y(start, left, building[start], building[left], tmp[0])
        if y > tmp[1]:
            tmp = (left, building[left])
            cnt[start] += 1


def find_right(start):
    if start + 2 > n - 1:
        return
    tmp = (start + 1, building[start + 1])
    for right in range(start + 2, n):
        y = get_y(start, right, building[start], building[right], tmp[0])
        if y > tmp[1]:
            tmp = (right, building[right])
            cnt[start] += 1


def get_y(x1, x2, y1, y2, x):
    return ((y2 - y1) / (x2 - x1)) * (x - x1) + y1


n = int(stdin.readline())
building = [*map(int, stdin.readline().split())]

cnt = [2] * n
cnt[0] = cnt[-1] = 1
for now in range(n):
    find_left(now)
    find_right(now)

print(0 if n == 1 else max(cnt))


# sol 2
from sys import stdin

n = int(stdin.readline())
building = [*map(int, stdin.readline().split())]

ans = 0
for x, y in enumerate(building):
    cnt = 0
    max_slope = -1e9
    min_slope = 1e9

    for next_x in range(x - 1, -1, -1):
        slope = (building[next_x] - y) / (next_x - x)
        if slope < min_slope:
            min_slope = slope
            cnt += 1

    for next_x in range(x + 1, n):
        slope = (building[next_x] - y) / (next_x - x)
        if slope > max_slope:
            max_slope = slope
            cnt += 1

    ans = max(ans, cnt)

print(ans)
