from sys import stdin

# 1
letter_1 = stdin.readline().rstrip()
letter_2 = stdin.readline().rstrip()
dp = [[0] * (len(letter_2) + 1) for _ in range(len(letter_1) + 1)]
for i in range(1, len(letter_1) + 1):
    for j in range(1, len(letter_2) + 1):
        if letter_1[i - 1] == letter_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[-1][-1])

##########################
#    memory: 55712KB     #
#    time:   580ms       #
##########################


# 2
letter_1 = stdin.readline().rstrip()
letter_2 = stdin.readline().rstrip()
dp = [0] * len(letter_2)
for let_1 in letter_1:
    cnt = 0
    for i, let_2 in enumerate(letter_2):
        if dp[i] > cnt:
            cnt = dp[i]
        elif let_1 == let_2:
            dp[i] = cnt + 1

print(max(dp))

##########################
#    memory: 31256KB     #
#    time:   212ms       #
##########################
