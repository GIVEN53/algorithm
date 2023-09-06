from sys import stdin
from itertools import permutations

perm = list(permutations("123456789", 3))
for _ in range(int(stdin.readline())):
    num, s, b = stdin.readline().split()
    filter = []
    for p in perm:
        strike = ball = 0
        for i, n in enumerate(num):
            if n == p[i]:
                strike += 1
            elif n in p:
                ball += 1
        if strike == int(s) and ball == int(b):
            filter.append(p)
    perm = filter

print(len(perm))

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################
