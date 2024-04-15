from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque(sorted(map(int, stdin.readline().split())))

tmp = deque([q.pop()])
ans = 0
while q:
    LL = abs(tmp[0] - q[0])
    RR = abs(tmp[-1] - q[-1])
    LR = abs(tmp[0] - q[-1])
    RL = abs(tmp[-1] - q[0])

    if LL >= RR and LL >= LR and LL >= RL:
        ans += LL
        tmp.appendleft(q.popleft())
    elif RR >= LL and RR >= LR and RR >= RL:
        ans += RR
        tmp.append(q.popleft())
    elif LR >= LL and LR >= RR and LR >= RL:
        ans += LR
        tmp.appendleft(q.pop())
    else:
        ans += RL
        tmp.append(q.pop())

print(ans)
