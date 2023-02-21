from sys import stdin
from heapq import heappop, heappush


n = int(stdin.readline())
task = []
for _ in range(n):
    d, w = map(int, stdin.readline().split())
    heappush(task, (-d, w))

possible_task, score = [], 0
for day in range(-task[0][0], 0, -1):
    while task and -task[0][0] >= day:
        heappush(possible_task, -heappop(task)[1])
    
    if possible_task:
        score += -heappop(possible_task)

print(score)
