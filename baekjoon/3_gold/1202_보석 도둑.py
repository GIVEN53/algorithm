from sys import stdin
from heapq import heappop, heappush


n, k = map(int, stdin.readline().split())
jewel = sorted([tuple(map(int, stdin.readline().split())) for _ in range(n)], key = lambda x:x[0])

c = sorted(int(stdin.readline()) for _ in range(k))

price = 0
tmp = []
for bag in c:
    while jewel and bag >= jewel[0][0]:
        heappush(tmp, -heappop(jewel)[1])
    if tmp:
        price += -heappop(tmp)

print(price)
