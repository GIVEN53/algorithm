from collections import deque
from sys import stdin

# 1
N, K = map(int, stdin.readline().split())

q = deque(i for i in range(1, N + 1))
ans = []
cnt = 1
while q:
    num = q.popleft()

    if cnt == K:
        ans.append(num)
        cnt = 1
    else:
        q.append(num)
        cnt += 1

print(str(ans).replace('[', '<').replace(']', '>'))


# 2
N, K = map(int, stdin.readline().split())

q = list(range(1, N + 1))
ans = []
idx = 0
while q:
    idx = (idx + K - 1) % len(q)
    ans.append(q.pop(idx))

print(str(ans).replace('[', '<').replace(']', '>'))
