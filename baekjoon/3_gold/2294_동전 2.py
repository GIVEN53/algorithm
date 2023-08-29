from sys import stdin

n, k = map(int, stdin.readline().split())
coins = set()
for _ in range(n):
    coin = int(stdin.readline())
    if coin <= k:
        coins.add(coin)

dp = [1e9] * (k + 1)
dp[0] = 0
for v in range(1, k + 1):
    for coin in coins:
        if v >= coin:
            dp[v] = min(dp[v], dp[v - coin] + 1)

print(dp[k] if dp[k] != 1e9 else -1)

##########################
#    memory: 31256KB     #
#    time:   368ms       #
##########################
