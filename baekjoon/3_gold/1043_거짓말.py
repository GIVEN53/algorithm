from collections import deque
from sys import stdin


# 1
def bfs(truth: deque, cnt):
    global truth_visited, impossible_party

    while truth:
        t = truth.popleft()

        for i in range(M):
            if impossible_party[i]:
                continue

            if t in party[i]:
                impossible_party[i] = True
                cnt -= 1
                for node in party[i]:
                    if not truth_visited[node]:
                        truth_visited[node] = True
                        truth.append(node)
    return cnt


N, M = map(int, stdin.readline().split())
truth = deque(map(int, stdin.readline().split()[1:]))

party = []
for _ in range(M):
    party.append(set(map(int, stdin.readline().split()[1:])))

truth_visited = [False] * (N + 1)
if truth:
    for i in truth:
        truth_visited[i] = True

impossible_party = [False] * M

print(bfs(truth, M))


# 2
N, M = map(int, stdin.readline().split())
truth = set(stdin.readline().split()[1:])

party = []
for _ in range(M):
    party.append(set(stdin.readline().split()[1:]))


for _ in range(M):
    for p in party:
        if truth & p:
            truth = truth.union(p)

cnt = 0
for p in party:
    if not p & truth:
        cnt += 1

print(cnt)
