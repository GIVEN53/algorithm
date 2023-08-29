from sys import stdin, setrecursionlimit


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


setrecursionlimit(10**6)
n, m = map(int, stdin.readline().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    operator, a, b = map(int, stdin.readline().split())
    if operator == 0:
        union(a, b)
    elif operator == 1:
        print("YES") if find(a) == find(b) else print("NO")

##########################
#    memory: 76720KB     #
#    time:   304ms       #
##########################
