from heapq import heappop, heappush
from sys import stdin


# 1 4740ms
def insert_pay(idx, pay):
    if not ans[idx]:
        ans[idx] = pay
    else:
        min_idx = 1
        for i in range(1, idx + 1):
            if ans[i] < ans[min_idx]:
                min_idx = i
        ans[min_idx] = pay


n = int(stdin.readline())
univ = []
for _ in range(n):
    p, d = map(int, stdin.readline().split())
    heappush(univ, (d, p))

ans = [0] * (n + 1)
next = 1
while univ:
    day, pay = heappop(univ)

    if day <= n:
        insert_pay(day, pay)
        next = day + 1
    else:
        insert_pay(next, pay)
        next += 1
print(sum(ans))


# 2 56ms
n = int(stdin.readline())
univ = sorted([tuple(map(int, stdin.readline().split()))
              for _ in range(n)], key=lambda x: x[1])

ans = []
for pay, day in univ:
    heappush(ans, pay)

    if day < len(ans):
        heappop(ans)
print(sum(ans))
