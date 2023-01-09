from collections import deque
from sys import stdin


def get_seq(q: deque, importances, M):
    target = q[M]
    q[M] = -1
    cnt = 1
    while q:
        doc = q.popleft()
        max_importance = importances[0]

        if doc == -1 and max_importance == target:
            print(cnt)
            break
        elif doc == max_importance:
            importances.remove(max_importance)
            cnt += 1
        else:
            q.append(doc)


T = int(stdin.readline())
for _ in range(T):
    _, M = map(int, stdin.readline().split())
    q = deque(map(int, stdin.readline().split()))
    importances = sorted(q, reverse=True)
    get_seq(q, importances, M)
