from collections import deque
from sys import stdin

def bfs(n):
    q = deque([n])

    while q:
        x = q.popleft()

        if x == k:
            return visited[x]
        
        for nx in (x - 1, x + 1, x * 2):
            if nx < 0 or nx > 200000:
                continue

            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)

n, k = map(int, stdin.readline().split())

visited = [-1] * 200001
visited[n] = 0
print(bfs(n))
