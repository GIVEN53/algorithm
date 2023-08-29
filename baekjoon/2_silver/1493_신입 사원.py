from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    interview_rank = [0] * n
    for _ in range(n):
        a, b = map(int, stdin.readline().split())
        interview_rank[a - 1] = b - 1

    min_interview_rank = interview_rank[0]
    cnt = 1
    for rank in interview_rank[1:]:
        if min_interview_rank > rank:
            min_interview_rank = rank
            cnt += 1

    print(cnt)

##########################
#    memory: 35892KB     #
#    time:   2216ms      #
##########################
