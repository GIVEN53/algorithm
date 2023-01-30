from sys import stdin, setrecursionlimit


def get_min_blank(idx):
    global dp

    if dp[idx] < 1e9:
        return dp[idx]

    blank = m - names[idx]
    next = idx + 1
    while blank >= 0:
        if next == n:
            dp[idx] = 0
            break

        dp[idx] = min(dp[idx], blank ** 2 + get_min_blank(next))
        blank -= names[next] + 1
        next += 1

    return dp[idx]


setrecursionlimit(10 ** 6)
n, m = map(int, stdin.readline().split())
names = [int(stdin.readline()) for _ in range(n)]
dp, dp[-1] = [1e9] * n, 0

print(get_min_blank(0))
