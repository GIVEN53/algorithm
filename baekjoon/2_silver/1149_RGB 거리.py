from sys import stdin

n = int(stdin.readline())
house = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    house[i][0] += min(house[i - 1][1], house[i - 1][2])
    house[i][1] += min(house[i - 1][0], house[i - 1][2])
    house[i][2] += min(house[i - 1][0], house[i - 1][1])

print(min(house[-1]))

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################
