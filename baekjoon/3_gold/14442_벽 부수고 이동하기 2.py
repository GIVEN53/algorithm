from sys import stdin
from collections import deque


def bfs():
    q = deque([(0, 0, 1)])
    visited[0][0] = 0

    while q:
        r, c, moved = q.popleft()
        if r == n - 1 and c == m - 1:
            return moved

        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc):
                continue

            b = visited[r][c] + arr[nr][nc]
            if b <= k and b < visited[nr][nc]:
                q.append((nr, nc, moved + 1))
                visited[nr][nc] = b

    return -1


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


n, m, k = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]

visited = [[k + 1] * m for _ in range(n)]
direction = [1, 0, -1, 0]
print(bfs())
