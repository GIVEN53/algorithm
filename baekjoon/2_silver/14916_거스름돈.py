from sys import stdin

n = int(stdin.readline())
dp = [1e9] * (n + 1)
dp[0] = 0
for i in range(2, n + 1):
    for coin in [2, 5]:
        if i - coin < 0:
            continue
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[-1] if dp[-1] != 1e9 else -1)

##########################
#    memory: 35108KB     #
#    time:   144ms       #
##########################
