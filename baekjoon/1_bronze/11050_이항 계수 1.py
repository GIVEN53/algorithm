from sys import stdin
# n!/k!(n-k)!

# 1
n, k = map(int, stdin.readline().split())
dp = [1] * (n + 1)

for i in range(1, n+1):
    dp[i] = dp[i - 1] * i

print(dp[n]//(dp[k] * dp[n - k]))


# 2
n, k = map(int, stdin.readline().split())

ans = 1
for i in range(n - k + 1, n + 1):
    ans *= i

for i in range(1, k + 1):
    ans //= i

print(ans)


# 3
def fac(n):
    global dp
    if n <= 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = n * fac(n - 1)
    return dp[n]


n, k = map(int, stdin.readline().split())
dp = [0] * (n + 1)
print(fac(n) // (fac(k) * fac(n - k)))
