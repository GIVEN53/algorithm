from sys import stdin, setrecursionlimit


def dfs(height, width):
    land[height][width] = 0

    for d in direction:
        nh, nw = height + d[0], width + d[1]
        if is_out_of_range(nh, nw) or not land[nh][nw]:
            continue

        dfs(nh, nw)


def is_out_of_range(height, width):
    return height < 0 or width < 0 or height >= h or width >= w


setrecursionlimit(10**6)
while True:
    w, h = map(int, stdin.readline().split())
    if w == h == 0:
        break

    land = [list(map(int, stdin.readline().split())) for _ in range(h)]

    direction = [(1, 0), (0, -1), (-1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    cnt = 0
    for height in range(h):
        for width in range(w):
            if land[height][width]:
                dfs(height, width)
                cnt += 1
    print(cnt)

##########################
#    memory: 31588KB     #
#    time:   80ms        #
##########################
