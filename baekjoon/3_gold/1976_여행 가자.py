from sys import stdin


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)

    if b < a:
        a, b = b, a
    parent[b] = a


n, m = int(stdin.readline()), int(stdin.readline())

parent = [i for i in range(n)]
for i in range(n):
    connected = list(map(int, stdin.readline().split()))
    for j in range(n):
        if connected[j]:
            union(i, j)

city = list(map(int, stdin.readline().split()))
ans = "YES"
for i in range(1, m):
    if parent[city[0] - 1] != parent[city[i] - 1]:
        ans = "NO"
        break

print(ans)
