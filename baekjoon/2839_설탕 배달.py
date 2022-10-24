n = int(input())
dp = [5000 for i in range(n+1)]
dp[0] = 0

sugar = [3, 5]

for i in sugar :
  for j in range(i, n+1) :
    dp[j] = min(dp[j], dp[j - i] + 1)

if dp[n] == 5000 :
  print(-1)
else :
  print(dp[n])

# n = 10
# dp 0 1 2 3 4 5 6 7 8 9 10
# 3  0 x x 1 x x 2 x x 3 x
# 5  0 x x x x 1 x x 2 x 2