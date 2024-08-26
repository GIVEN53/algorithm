# 1
from sys import stdin
from collections import deque


def bfs():
    q = deque([(1, 0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        cnt, bk, r, c = q.popleft()

        if r == n - 1 and c == m - 1:
            return cnt

        time = cnt % 2
        cnt += 1
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]

            if out_of_range(nr, nc):
                continue

            nbk = bk + arr[nr][nc]
            if nbk <= k and visited[nbk][nr][nc] > cnt:
                if not arr[nr][nc] or time:
                    q.append((cnt, nbk, nr, nc))
                    visited[nbk][nr][nc] = cnt
                else:
                    q.append((cnt, bk, r, c))

    return -1


def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


n, m, k = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
visited = [[[1e9] * m for _ in range(n)] for _ in range(k + 1)]
direction = [1, 0, -1, 0]

print(bfs())


# 2
from sys import stdin
from collections import deque


def bfs():
    q = deque([(1, 0, 0, 0)])
    visited[0][0] = 0

    while q:
        cnt, bk, r, c = q.popleft()

        if r == n - 1 and c == m - 1:
            return cnt

        time = cnt % 2
        cnt += 1
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]

            if out_of_range(nr, nc):
                continue

            nbk = bk + arr[nr][nc]
            if nbk <= k and visited[nr][nc] > nbk:
                if not arr[nr][nc] or time:
                    q.append((cnt, nbk, nr, nc))
                    visited[nr][nc] = nbk
                else:
                    q.append((cnt, bk, r, c))

    return -1


def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


n, m, k = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
visited = [[k + 1] * m for _ in range(n)]
direction = [1, 0, -1, 0]

print(bfs())
