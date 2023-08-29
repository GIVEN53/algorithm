from sys import stdin


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt, now = 1, house[0] + mid
        for h in house:
            if h >= now:
                cnt += 1
                now = h + mid

        if cnt >= c:
            start = mid + 1
        else:
            end = mid - 1
    return end


n, c = map(int, stdin.readline().split())
house = [int(stdin.readline()) for _ in range(n)]
house.sort()

start, end = 1, (house[-1] - house[0]) // (c - 1)
print(binary_search(start, end))

##########################
#    memory: 38984KB     #
#    time:   128ms       #
##########################
