from collections import deque
from sys import stdin


T = int(stdin.readline())
for _ in range(T):
    p = stdin.readline().rstrip().replace('RR', '')
    n = int(stdin.readline())
    q = deque(stdin.readline()[1:-2].split(','))

    reverse = 0
    for func in p:
        if func == 'R':
            reverse += 1
        elif func == 'D' and n > 0:
            n -= 1
            if reverse % 2 == 0:
                q.popleft()
            else:
                q.pop()
        elif func == 'D' and n == 0:
            reverse = -1
            break

    if reverse == -1:
        print('error')
    elif reverse % 2 == 0:
        print('[' + ','.join(q) + ']')
    else:
        q.reverse()
        print('[' + ','.join(q) + ']')
