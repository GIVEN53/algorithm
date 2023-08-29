from sys import stdin

n = int(stdin.readline())
triangle = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[-1]))

##########################
#    memory: 35620KB     #
#    time:   128ms       #
##########################
