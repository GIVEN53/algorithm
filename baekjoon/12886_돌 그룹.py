from collections import deque


def bfs(a, b):
    global visited, tot
    q = deque()
    q.append((a, b))
    visited[a][b] = True

    while q:
        a, b = q.popleft()
        c = tot - a - b
        if a == b == c:
            return 1

        for x, y in (a, b), (a, c):
            if x == y:
                continue
            x, y = 2 * x, y - x
            x, y, _ = sorted((x, y, tot - x - y))
            if not visited[x][y]:
                q.append((x, y))
                visited[x][y] = True
    return 0


a, b, c = map(int, input().split())
a, b, c = sorted((a, b, c))
tot = a + b + c
visited = [[False] * (tot+1) for _ in range(tot+1)]

if tot % 3 != 0:
    print(0)
else:
    print(bfs(a, b))
