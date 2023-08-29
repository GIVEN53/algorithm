from sys import stdin

# 1
n, k = map(int, stdin.readline().split())
bag = [(0, 0)] + [tuple(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w, v = bag[i]
    for j in range(1, k + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[n][k])

##########################
#    memory: 227172KB    #
#    time:   4688ms      #
##########################


# 2
n, k = map(int, stdin.readline().split())
bag = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
bag.sort(reverse=True)

dp = {0: 0}
for w, v in bag:
    tmp = {}
    for value, weight in dp.items():
        if (w_sum := w + weight) < dp.get(v_sum := v + value, k + 1):
            tmp[v_sum] = w_sum
    dp.update(tmp)

print(max(dp.keys()))

##########################
#    memory: 34744KB     #
#    time:   448ms       #
##########################
