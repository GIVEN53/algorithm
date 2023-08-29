from sys import stdin, setrecursionlimit


def dfs(now):
    for next, weight in tree[now]:
        if distance[next] != -1:
            continue
        distance[next] = distance[now] + weight
        dfs(next)


setrecursionlimit(10**6)
n = int(stdin.readline())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, w = map(int, stdin.readline().split())
    tree[a - 1].append((b - 1, w))
    tree[b - 1].append((a - 1, w))

distance = [-1] * n
distance[0] = 0
dfs(0)
max_node = distance.index(max(distance))

distance = [-1] * n
distance[max_node] = 0
dfs(max_node)
print(max(distance))

##########################
#    memory: 35572KB     #
#    time:   76ms        #
##########################
