from sys import stdin
from itertools import combinations

while True:
    k, *s = stdin.readline().split()
    if k == "0":
        break

    for comb in combinations(s, 6):
        print(*comb)

    print()

##########################
#    memory: 31256KB     #
#    time:   52ms        #
##########################
