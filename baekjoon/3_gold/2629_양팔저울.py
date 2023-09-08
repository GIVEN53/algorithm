from sys import stdin

# 1 dp
n = int(stdin.readline())
weight = [*map(int, stdin.readline().split())]
m = int(stdin.readline())
bead = [*map(int, stdin.readline().split())]

dp = [[0] * 40001 for _ in range(n)]
dp[0][weight[0]] = 1
for i in range(1, n):
    dp[i][weight[i]] = 1
    for j in range(1, 40001):
        if dp[i - 1][j] == 1:
            dp[i][j] = 1
            dp[i][abs(weight[i] - j)] = 1
        if dp[i - 1][abs(weight[i] - j)] == 1:
            dp[i][j] = 1

for i in range(m):
    print("Y" if dp[-1][bead[i]] else "N", end=" ")

##########################
#    memory: 40732KB     #
#    time:   388ms       #
##########################


# 2 set
from sys import stdin

n = int(stdin.readline())
weight = [*map(int, stdin.readline().split())]
m = int(stdin.readline())
bead = [*map(int, stdin.readline().split())]

dp = {0}
for w in weight:
    tmp = set()

    for d in dp:
        tmp.add(abs(w - d))
        tmp.add(w + d)
    dp = dp.union(tmp)

print(*["Y" if b in dp else "N" for b in bead])

##########################
#    memory: 31256KB     #
#    time:   48ms        #
##########################
