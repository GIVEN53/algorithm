from sys import stdin
from itertools import combinations
from collections import defaultdict


def get_sum_subset(seq):
    subset = defaultdict(int)
    for i in range(1, n + 1):
        for comb in combinations(seq, i):
            subset[sum(comb)] += 1
    return subset


n, s = map(int, stdin.readline().split())
seq = [*map(int, stdin.readline().split())]

left_subset = get_sum_subset(seq[: n // 2])
right_subset = get_sum_subset(seq[n // 2 :])

ans = left_subset[s] + right_subset[s]
for ls in left_subset:
    if s - ls in right_subset:
        ans += left_subset[ls] * right_subset[s - ls]

print(ans)

##########################
#    memory: 121532KB    #
#    time:   1164ms      #
##########################
