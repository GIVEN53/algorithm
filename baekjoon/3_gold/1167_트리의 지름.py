from sys import stdin


def dfs(now, diameter):
    global visited

    for next, d in graph[now].items():
        if visited[next] == -1:
            visited[next] = diameter + d
            dfs(next, visited[next])


V = int(stdin.readline())
graph = [{} for _ in range(V + 1)]

for _ in range(V):
    edges = [*map(int, stdin.readline().split()[:-1])]
    node = edges[0]

    for i in range(2, len(edges), 2):
        graph[node][edges[i - 1]] = edges[i]

visited = [-1] * (V + 1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (V + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))
