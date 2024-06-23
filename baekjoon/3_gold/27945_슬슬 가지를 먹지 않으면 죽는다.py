from sys import stdin


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if b < a:
        a, b = b, a
    parent[a] = b
    return True


n, m = map(int, stdin.readline().split())
graph = []
for _ in range(m):
    a, b, t = map(int, stdin.readline().split())
    if a > b:
        a, b = b, a
    graph.append((t, a - 1, b - 1))
graph.sort()

parent = [i for i in range(n)]
day = 1
for i in range(n - 1):
    t, a, b = graph[i]
    if day != t:
        break
    if not union(a, b):
        break
    day += 1

print(day)
