from sys import stdin


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)

    if a == b:
        return False

    if b < a:
        a, b = b, a
    parent[a] = b
    return True


n, m = map(int, stdin.readline().split())
edges = []
for i in range(m):
    u, v, c = map(int, stdin.readline().split())
    edges.append((c, u, v, i + 1))

if m == n - 1:  # 스패닝 트리 한 개 존재
    print("NO")
else:  # m >= n일 경우 최소 3개 이상
    edges.sort()
    parent = [i for i in range(n + 1)]
    tmp = None
    for _, u, v, i in edges:
        if not union(u, v):  # MST
            tmp = (u, v, i)  # MST에 포함되지 않은 간선 저장
            break

    parent = [i for i in range(n + 1)]
    union(tmp[0], tmp[1])  # MST에 포함되지 않았던 간선 포함해서 다시 MST
    ans = [tmp[2]]
    for _, u, v, i in edges:
        if union(u, v):
            ans.append(i)

    print("YES")
    print(*ans)
