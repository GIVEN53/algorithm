from sys import stdin


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


def dfs(v):
    visited[v] = True
    for next, p, q in ratio[v]:
        if not visited[next]:
            ingredient[next] = ingredient[v] * q // p
            dfs(next)


n = int(stdin.readline())
ratio = [[] for _ in range(n)]
lcm = 1
for _ in range(n - 1):
    a, b, p, q = map(int, stdin.readline().split())
    ratio[a].append((b, p, q))
    ratio[b].append((a, q, p))
    lcm *= p * q // get_gcd(p, q)

ingredient = [0] * n
ingredient[0] = lcm
visited = [False] * n
dfs(0)

mgcd = ingredient[0]
for i in range(1, n):
    mgcd = get_gcd(mgcd, ingredient[i])

for i in range(n):
    ingredient[i] //= mgcd

print(*ingredient)
