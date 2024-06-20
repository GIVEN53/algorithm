from sys import stdin
from math import ceil

n, k = map(int, stdin.readline().split())
dp = [0] * (n + 1)
for i in range(min(6, n + 1)):
    dp[i] = i

for i in range(6, n + 1):
    prev = ceil(i * 2 / 3)
    if prev + prev // 2 == i:
        dp[i] = min(dp[prev], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1

if dp[n] <= k:
    print("minigimbob")
else:
    print("water")
