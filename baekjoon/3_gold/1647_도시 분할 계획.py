from sys import stdin


def find(x):
    if x != nodes[x]:
        nodes[x] = find(nodes[x])
    return nodes[x]


def union(a, b):
    if a < b:
        nodes[b] = a
    else:
        nodes[a] = b


n, m = map(int, stdin.readline().split())
edges = []
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    edges.append((c, a, b))
edges.sort(key=lambda x: x[0])

nodes = [i for i in range(n + 1)]
res = cnt = 0
for cost, a, b in edges:
    if cnt == n - 2:
        break

    a, b = find(a), find(b)
    if a != b:
        union(a, b)
        res += cost
        cnt += 1

print(res)

##########################
#    memory: 208536KB    #
#    time:   2384ms      #
##########################
