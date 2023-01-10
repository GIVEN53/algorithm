from sys import stdin

T = int(stdin.readline())
floor = []
ho = []
for _ in range(T):
    floor.append(int(stdin.readline()))
    ho.append(int(stdin.readline()))

dp = [i for i in range(15)] + [0] * 14 * max(floor)

for i in range(15, len(dp)):
    if (i - 1) % 14 == 0:
        dp[i] = 1
    else:
        dp[i] = dp[i - 14] + dp[i - 1]

for i in range(T):
    idx = 14 * floor[i] + ho[i]
    print(dp[idx])
