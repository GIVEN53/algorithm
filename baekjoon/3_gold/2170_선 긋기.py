from sys import stdin

n = int(stdin.readline())
xy = [list(map(int, stdin.readline().split())) for _ in range(n)]
xy.sort()

total = 0
start, end = xy[0]
for x, y in xy[1:]:
    if x > end:
        total += end - start
        start = x
        end = y
    elif y > end:
        end = y

print(total + (end - start))

##########################
#    memory: 239868KB    #
#    time:   4212ms      #
##########################
