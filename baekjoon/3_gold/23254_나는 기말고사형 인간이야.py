from sys import stdin
from heapq import heappush, heappop

n, m = map(int, stdin.readline().split())
scores = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
unit_scores = []
for i in range(m):
    heappush(unit_scores, (-b[i], i))

left_hours = 24 * n
while unit_scores and left_hours > 0:
    unit_score, i = heappop(unit_scores)
    unit_score *= -1
    hours = (100 - scores[i]) // unit_score
    if hours > left_hours:
        hours = left_hours
    scores[i] += hours * unit_score
    left_score = 100 - scores[i]
    if 0 < left_score < unit_score:
        heappush(unit_scores, (-left_score, i))

    left_hours -= hours

print(sum(scores))
