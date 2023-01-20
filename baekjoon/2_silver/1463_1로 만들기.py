from sys import stdin


# 1
n = int(stdin.readline())

dp = [0] * (n + 1)
for i in range(2, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i // 2], dp[i // 3]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp[n])


# 2
def reculsion(n):
    global dp

    if n in dp.keys():
        return dp[n]
    
    if n % 2 == 0 and n % 3 == 0:
        dp[n] = min(reculsion(n // 2), reculsion(n // 3)) + 1
    elif n % 3 == 0:
        dp[n] = min(reculsion(n // 3), reculsion(n - 1)) + 1
    elif n % 2 == 0:
        dp[n] = min(reculsion(n // 2), reculsion(n - 1)) + 1
    else:
        dp[n] = reculsion(n - 1) + 1
    
    return dp[n]


n = int(stdin.readline())
dp = {1 : 0, 2 : 1, 3 : 1}
print(reculsion(n))
