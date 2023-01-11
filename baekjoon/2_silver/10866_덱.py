from collections import deque
from sys import stdin

N = int(stdin.readline())

q = deque()
for _ in range(N):
    command = stdin.readline().rstrip()

    if command == 'pop_front':
        print(q.popleft() if q else -1)
    elif command == 'pop_back':
        print(q.pop() if q else -1)
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        print(0 if q else 1)
    elif command == 'front':
        print(q[0] if q else -1)
    elif command == 'back':
        print(q[-1] if q else -1)
    else:
        c, num = command.split()
        if c == 'push_front':
            q.appendleft(int(num))
        else:  # c == 'push_back'
            q.append(int(num))
