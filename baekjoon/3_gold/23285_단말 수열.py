from sys import stdin
from heapq import heappop, heappush

n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

degree = [0] * (n + 1)
for s in seq:
    degree[s] += 1

leafs = []
for i in range(1, n + 1):
    if degree[i] == 0:
        heappush(leafs, i)

edges = []
for s in seq:
    leaf = heappop(leafs)
    edges.append((leaf, s) if leaf < s else (s, leaf))
    degree[s] -= 1
    if degree[s] == 0:
        heappush(leafs, s)

last = seq[-1]
edges.append((last, n))
edges.sort()
for e in edges:
    print(*e)
