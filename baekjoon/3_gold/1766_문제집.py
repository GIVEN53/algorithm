from sys import stdin
from heapq import heappop, heappush


n, m = map(int, stdin.readline().split())
problem = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    problem[a].append(b)
    degree[b] += 1

q = []
for i in range(1, n + 1):
    if degree[i] == 0:
        heappush(q, i)

res = []
while q:
    num = heappop(q)
    res.append(num)

    for i in problem[num]:
        degree[i] -= 1
        if degree[i] == 0:
            heappush(q, i)

print(*res)

##########################
#    memory: 40768KB     #
#    time:   224ms       #
##########################
