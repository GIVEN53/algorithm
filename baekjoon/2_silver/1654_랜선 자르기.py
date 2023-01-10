def search(low, high):
    if low > high:
        return high
    
    cnt = 0
    mid = (low+high) // 2
    for i in lengths:
        cnt += i//mid
    if cnt >= N:
        return search(mid + 1, high)
    else:
        return search(low, mid - 1)

from sys import stdin
K, N = map(int, stdin.readline().split())
lengths = [int(stdin.readline().rstrip()) for _ in range(K)]

max_cm = search(1, max(lengths))
print(max_cm)
