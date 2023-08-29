from sys import stdin
from collections import deque

n = int(stdin.readline())
crane = sorted(list(map(int, stdin.readline().split())), reverse=True)
_ = int(stdin.readline())
box = deque(sorted(map(int, stdin.readline().split()), reverse=True))

if box[0] > crane[0]:
    print(-1)
    exit()

batch_crane = [0] * n
while box:
    b = box.popleft()
    worker, min_batch = 0, batch_crane[0]
    for i in range(1, n):
        if crane[i] >= b:
            if batch_crane[i] < min_batch:
                worker = i
                min_batch = batch_crane[i]
        else:
            break
    batch_crane[worker] += 1

print(max(batch_crane))

##########################
#    memory: 34160KB     #
#    time:   68ms        #
##########################
