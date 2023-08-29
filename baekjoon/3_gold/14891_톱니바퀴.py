from sys import stdin
from collections import deque


def dfs(now, d):
    global visited

    if visited[now] == cnt:
        return

    visited[now] = cnt
    left = gears[now][6]
    right = gears[now][2]

    if now - 1 >= 0 and left != gears[now - 1][2]:
        dfs(now - 1, d * -1)

    if now + 1 < 4 and right != gears[now + 1][6]:
        dfs(now + 1, d * -1)

    if d == 1:
        gears[now].appendleft(gears[now].pop())
    else:
        gears[now].append(gears[now].popleft())


gears = [deque(stdin.readline().rstrip()) for _ in range(4)]
k = int(stdin.readline())

visited = [-1] * 4
cnt = 0
while cnt < k:
    now, d = map(int, stdin.readline().split())
    dfs(now - 1, d)
    cnt += 1

res = sum(1 << i if gears[i][0] == "1" else 0 for i in range(4))
print(res)

##########################
#    memory: 34140KB     #
#    time:   64ms        #
##########################
