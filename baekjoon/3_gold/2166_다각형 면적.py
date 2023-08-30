from sys import stdin

n = int(stdin.readline())
xy = [list(map(int, stdin.readline().split())) for _ in range(n)]
xy.append(xy[0])
ans = sum(xy[i][0] * xy[i + 1][1] - xy[i][1] * xy[i + 1][0] for i in range(n))
print(abs(round(ans / 2, 1)))

##########################
#    memory: 33300KB     #
#    time:   56ms        #
##########################
