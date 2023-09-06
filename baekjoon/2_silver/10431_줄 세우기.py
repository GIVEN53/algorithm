from sys import stdin

for _ in range(int(stdin.readline())):
    t, *student = map(int, stdin.readline().split())

    cnt = 0
    for now in range(1, 20):
        for prev in range(now - 1, -1, -1):
            if student[now] > student[prev]:
                break
            tmp = student[prev]
            student[prev] = student[now]
            student[now] = tmp
            cnt += 1
            now -= 1

    print(t, cnt)


##########################
#    memory: 31256KB     #
#    time:   84ms        #
##########################
