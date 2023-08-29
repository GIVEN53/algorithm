from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
house = []
chicken = []
for i in range(n):
    city = list(map(int, stdin.readline().split()))
    for j in range(n):
        if city[j] == 1:
            house.append((i, j))
        elif city[j] == 2:
            chicken.append((i, j))

res = 1e9
for chicken_pick in combinations(chicken, m):
    total_chicken_dist = 0
    for hr, hc in house:
        chicken_dist = 1e9
        for cr, cc in chicken_pick:
            chicken_dist = min(chicken_dist, abs(hr - cr) + abs(hc - cc))
        total_chicken_dist += chicken_dist
    res = min(res, total_chicken_dist)

print(res)

##########################
#    memory: 31256KB     #
#    time:   612ms       #
##########################
