from sys import stdin


def bellman_ford(start):
    distances = [1e9] * n
    distances[start] = 0
    for k in range(n):
        for i in range(n):
            for next, next_dist in road[i]:
                dist = distances[i] + next_dist
                if distances[next] > dist:
                    distances[next] = dist
                    if k == n - 1:
                        return True
    return False


tc = int(stdin.readline())
for _ in range(tc):
    n, m, w = map(int, stdin.readline().split())
    road = [[] for _ in range(n)]
    for _ in range(m):
        s, e, t = map(int, stdin.readline().split())
        road[s - 1].append((e - 1, t))
        road[e - 1].append((s - 1, t))

    for _ in range(w):
        s, e, t = map(int, stdin.readline().split())
        road[s - 1].append((e - 1, -t))

    print("YES" if bellman_ford(0) else "NO")

##########################
#    memory: 31256KB     #
#    time:   1068ms      #
##########################
