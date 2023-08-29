from sys import stdin


def cut(r, c, n):
    global color

    now = papers[r][c]
    h = n // 2
    for i in range(r, r + n):
        for j in range(c, c + n):
            if papers[i][j] != now:
                cut(r, c, h)
                cut(r + h, c, h)
                cut(r, c + h, h)
                cut(r + h, c + h, h)
                return

    color[now] += 1


n = int(stdin.readline())
papers = [list(map(int, stdin.readline().split())) for _ in range(n)]

color = [0, 0]
cut(0, 0, n)
print(*color, sep="\n")

##########################
#    memory: 31256KB     #
#    time:   52ms        #
##########################
