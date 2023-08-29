from sys import stdin

dragon = [[False] * 101 for _ in range(101)]
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for _ in range(int(stdin.readline())):
    x, y, d, g = map(int, stdin.readline().split())

    dragon[y][x] = True
    y += direction[d][0]
    x += direction[d][1]
    dragon[y][x] = True

    dir = [d]
    for _ in range(g):
        for i in range(len(dir) - 1, -1, -1):
            next_d = (dir[i] + 1) % 4
            y += direction[next_d][0]
            x += direction[next_d][1]
            dir.append(next_d)
            dragon[y][x] = True

square_cnt = 0
for i in range(100):
    for j in range(100):
        if (
            dragon[i][j]
            and dragon[i][j + 1]
            and dragon[i + 1][j]
            and dragon[i + 1][j + 1]
        ):
            square_cnt += 1

print(square_cnt)

##########################
#    memory: 31256KB     #
#    time:   48ms        #
##########################
