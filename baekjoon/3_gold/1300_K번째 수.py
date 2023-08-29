from sys import stdin


def get_cnt(mid):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid // i, n)

    return cnt


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2

        if get_cnt(mid) < k:
            start = mid + 1
        else:
            end = mid - 1

    return start


n, k = int(stdin.readline()), int(stdin.readline())

print(binary_search(1, k))

##########################
#    memory: 31256KB     #
#    time:   672ms       #
##########################
