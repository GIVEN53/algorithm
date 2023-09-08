from sys import stdin

n = int(stdin.readline())
arr = [*map(int, stdin.readline().split())]

dp = [1] * n
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

##########################
#    memory: 31256KB     #
#    time:   160ms       #
##########################
