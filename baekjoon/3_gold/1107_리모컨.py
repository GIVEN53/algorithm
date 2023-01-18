from sys import stdin


# 1
def get_count(is_up, target):
    if is_up:
        next = 1
    else:
        next = -1

    found_target = False
    while not found_target:
        for i in str(target):
            if i in broken:
                found_target = False
                target += next
                break
            found_target = True

        if target > 1000000:
            return min_count

    return abs(N - target) + len(str(target))


N, M = int(stdin.readline()), int(stdin.readline())
broken = set(stdin.readline().split())

min_count = abs(N - 100)
if N == 100:
    print(0)
elif M == 10:
    print(min_count)
elif M == 0:
    print(min(min_count, len(str(N))))
else:
    print(min(min_count, get_count(False, N), get_count(True, N)))


# 2
N, M = int(stdin.readline()), int(stdin.readline())
broken = set(stdin.readline().split())

min_count = abs(N - 100)
if N == 100:
    print(0)
elif M == 10:
    print(min_count)
elif M == 0:
    print(min(min_count, len(str(N))))
else:
    for i in range(1000001):
        for j in str(i):
            if j in broken:
                break
        else:
            min_count = min(min_count, abs(N - i) + len(str(i)))

    print(min_count)