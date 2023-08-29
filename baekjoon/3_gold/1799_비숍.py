from sys import stdin


def dfs(i, cnt):
    global tot
    if (d + 1 - i) // 2 + cnt < tot:
        return

    if i >= d:
        tot = max(tot, cnt)
        return

    for r, c in diag_up[i]:
        if not diag_down[r - c] and chess[r][c] == "1":
            diag_down[r - c] = True
            dfs(i + 2, cnt + 1)
            diag_down[r - c] = False
    dfs(i + 2, cnt)


n = int(stdin.readline())
chess = [stdin.readline().split() for _ in range(n)]
d = 2 * n - 1
diag_up = [[] for _ in range(d)]

for r in range(n):
    for c in range(n):
        diag_up[r + c].append((r, c))

diag_down = [0] * d
ans = tot = 0
dfs(0, 0)
ans += tot
tot = 0
dfs(1, 0)
ans += tot

print(ans)

##########################
#    memory: 31256KB     #
#    time:   60ms        #
##########################
