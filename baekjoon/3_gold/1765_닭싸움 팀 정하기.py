from sys import stdin


def find(x):
    if x != friend[x]:
        friend[x] = find(friend[x])
    return friend[x]


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return

    friend[b] = a


n, m = int(stdin.readline()), int(stdin.readline())
friend = [i for i in range(n + 1)]
enemy = [[] for _ in range(n + 1)]
for _ in range(m):
    letter, p, q = stdin.readline().split()
    p, q = int(p), int(q)
    if letter == "F":
        union(p, q)
    else:
        enemy[p].append(q)
        enemy[q].append(p)


for e in enemy:
    if len(e) > 1:
        a = e[0]
        for i in range(1, len(e)):
            union(a, e[i])

for i in range(1, n + 1):
    find(i)
print(len(set(friend)) - 1)

##########################
#    memory: 31256KB     #
#    time:   52ms        #
##########################
