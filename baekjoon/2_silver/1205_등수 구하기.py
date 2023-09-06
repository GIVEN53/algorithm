from sys import stdin

n, taesoo, p = map(int, stdin.readline().split())
if n == 0:
    print(1)
    exit()

score = sorted([*map(int, stdin.readline().split())] + [taesoo], reverse=True)
if taesoo == score[-1] and n == p:
    print(-1)
else:
    for i in range(len(score)):
        if taesoo == score[i]:
            print(i + 1)
            break

##########################
#    memory: 31256KB     #
#    time:   40ms        #
##########################
