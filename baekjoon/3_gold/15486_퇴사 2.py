from sys import stdin

N = int(stdin.readline())
day = []
price = []
for _ in range(N):
    T, P = map(int, stdin.readline().split())
    day.append(T)
    price.append(P)

dp = [0] * (N+1)
for i in range(N):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if i + day[i] <= N:
        if dp[i+day[i]] < dp[i] + price[i]:
            dp[i+day[i]] = dp[i] + price[i]

print(max(dp))
