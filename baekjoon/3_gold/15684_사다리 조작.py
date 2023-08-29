from sys import stdin


def is_same_vertical():
    for j in range(1, n + 1):
        start = j
        for i in range(1, h + 1):
            if ladder[i][j]:
                j = ladder[i][j]

        if start != j:
            return False
    return True


def dfs(cnt, depth, now):
    global res

    if is_same_vertical():
        res = min(res, cnt)
        return
    elif cnt == 3 or cnt >= res:
        return

    odd = 0
    for i in range(1, n + 1):
        if line[i] % 2:
            odd += 1
    if odd > 3 - cnt:
        return

    for i in range(depth, h + 1):
        k = now if depth == i else 1

        for j in range(k, n):
            if not ladder[i][j] and not ladder[i][j + 1]:
                ladder[i][j], ladder[i][j + 1] = j + 1, j
                line[j + 1] += 1
                dfs(cnt + 1, i, j + 2)
                ladder[i][j], ladder[i][j + 1] = 0, 0
                line[j + 1] -= 1


n, m, h = map(int, stdin.readline().split())
ladder = [[0] * (n + 1) for _ in range(h + 1)]
line = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    ladder[a][b] = b + 1
    ladder[a][b + 1] = b
    line[b + 1] += 1

res = 4
dfs(0, 1, 1)
print(res if res < 4 else -1)

##########################
#    memory: 31256KB     #
#    time:   320ms       #
##########################
