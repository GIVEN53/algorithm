def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return parent
        

def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key = lambda x:x[2])
    
    tot = 0
    for a, b, cost in costs:
        if find(parent, a) != find(parent, b):
            parent = union(parent, a, b)
            tot += cost
    
    return tot
