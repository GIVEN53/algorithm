from sys import stdin


def dfs(office, idx):
    global res

    if idx >= len(cctv):
        blind_spot = sum(o.count(0) for o in office)
        res = min(res, blind_spot)
        return

    r, c = cctv[idx]
    if office[r][c] == 1:
        for i in range(4):
            tmp_office = [o[:] for o in office]
            watch(tmp_office, r, c, direction[i][0], direction[i][1])
            dfs(tmp_office, idx + 1)
    elif office[r][c] == 2:
        for i in range(2):
            tmp_office = [o[:] for o in office]
            watch(tmp_office, r, c, direction[i][0], direction[i][1])
            watch(tmp_office, r, c, -direction[i][0], -direction[i][1])
            dfs(tmp_office, idx + 1)
    elif office[r][c] == 3:
        for i in range(4):
            tmp_office = [o[:] for o in office]
            watch(tmp_office, r, c, direction[i][0], direction[i][1])
            watch(
                tmp_office, r, c, direction[(i + 1) % 4][0], direction[(i + 1) % 4][1]
            )
            dfs(tmp_office, idx + 1)
    elif office[r][c] == 4:
        for i in range(4):
            tmp_office = [o[:] for o in office]
            watch(tmp_office, r, c, direction[i][0], direction[i][1])
            watch(
                tmp_office, r, c, direction[(i + 1) % 4][0], direction[(i + 1) % 4][1]
            )
            watch(
                tmp_office, r, c, direction[(i + 2) % 4][0], direction[(i + 2) % 4][1]
            )
            dfs(tmp_office, idx + 1)
    else:
        for i in range(4):
            watch(office, r, c, direction[i][0], direction[i][1])
        dfs(office, idx + 1)


def watch(office, r, c, dr, dc):
    while True:
        r += dr
        c += dc
        if r < 0 or r >= n or c < 0 or c >= m or office[r][c] == 6:
            break

        if office[r][c] == 0:
            office[r][c] = "#"


n, m = map(int, stdin.readline().split())
office = []
cctv = []
for i in range(n):
    o = list(map(int, stdin.readline().split()))
    for j in range(m):
        if 0 < o[j] < 6:
            cctv.append((i, j))
    office.append(o)

res = 1e9
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dfs(office, 0)

print(res)

##########################
#    memory: 31256KB     #
#    time:   344ms       #
##########################
