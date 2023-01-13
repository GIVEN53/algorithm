from collections import deque
from sys import stdin


# 1 queue, bfs
def topological_sort():
    q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        print(node, end=' ')

        for i in graph[node]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)


N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    in_degree[b] += 1

topological_sort()


# 2 stack, bfs
def topological_sort():
    stack = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            stack.append(i)

    while stack:
        node = stack.pop()
        print(node, end=' ')

        for i in graph[node]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                stack.append(i)


N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    in_degree[b] += 1

topological_sort()
