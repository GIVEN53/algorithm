from sys import stdin
from collections import deque


def bfs(a, b):
    visited = [False] * (n + 1)
    visited[a] = True
    q = deque()
    for x in family[a]:
        q.append((x, 1))

    while q:
        x, cnt = q.popleft()
        for y in family[x]:
            if visited[y]:
                continue
            if y == b:
                return cnt + 1
            visited[y] = True
            q.append((y, cnt + 1))

    return -1


n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
m = int(stdin.readline())
family = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    family[x].append(y)
    family[y].append(x)

print(bfs(a, b))

##########################
#    memory: 34176KB     #
#    time:   68ms        #
##########################
