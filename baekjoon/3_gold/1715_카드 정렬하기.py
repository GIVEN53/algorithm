from heapq import heappop, heappush
from sys import stdin

n = int(stdin.readline())
cards = sorted([int(stdin.readline()) for _ in range(n)])

cnt = 0
comparison = 0
ans = 0
while cards:
    comparison += heappop(cards)
    cnt += 1

    if cnt % 2 == 0:
        heappush(cards, comparison)
        ans += comparison
        comparison = 0

print(ans)
