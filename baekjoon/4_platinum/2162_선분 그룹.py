from sys import stdin


def ccw(x1, y1, x2, y2, x3, y3):
    # return x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3)
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def is_crossed(line_1, line_2):
    x1, y1, x2, y2 = line_1
    x3, y3, x4, y4 = line_2
    ccw_1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    ccw_2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if ccw_1 == ccw_2 == 0:
        return (
            min(x1, x2) <= max(x3, x4)
            and min(x3, x4) <= max(x1, x2)
            and min(y1, y2) <= max(y3, y4)
            and min(y3, y4) <= max(y1, y2)
        )
    return ccw_1 <= 0 and ccw_2 <= 0


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b


n = int(stdin.readline())
line = [list(map(int, stdin.readline().split())) for _ in range(n)]
parent = [i for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if is_crossed(line[i], line[j]):
            union(i, j)

ans = set(find(i) for i in range(n))
print(len(ans))
print(max(parent.count(i) for i in ans))

##########################
#    memory: 32276KB     #
#    time:   4620ms      #
##########################
