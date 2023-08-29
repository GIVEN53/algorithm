from sys import stdin

letter = stdin.readline().rstrip()
n = len(letter)
palindrome = [[0] * n for _ in range(n)]
dp = [2500] * (n + 1)
dp[-1] = 0
for e in range(n):
    for s in range(e + 1):
        if letter[s] == letter[e] and (e - s < 2 or palindrome[s + 1][e - 1]):
            palindrome[s][e] = 1
            dp[e] = min(dp[e], dp[s - 1] + 1)

print(dp[n - 1])

##########################
#    memory: 79548KB     #
#    time:   2112ms      #
##########################
