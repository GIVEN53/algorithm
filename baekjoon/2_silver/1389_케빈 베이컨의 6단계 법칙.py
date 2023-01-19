from sys import stdin


N, M = map(int, stdin.readline().split())

graph = [[1e9] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N + 1):
    for j in range(0, N + 1):
        if i == j or j == 0:
            graph[i][j] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_bacon = 5000
person = 0
for i in range(1, N + 1):
    bacon = sum(graph[i])
    if bacon < min_bacon:
        min_bacon = bacon
        person = i

print(person)
