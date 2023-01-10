from collections import Counter
from sys import stdin

_, M = map(int, stdin.readline().split())
trees = Counter(map(int, stdin.readline().split()))

max_meter = 0
low = 0
high = max(trees)

while low <= high:
    mid = (low + high) // 2
    cutting_height = sum((i - mid) * cnt for i, cnt in trees.items() if i > mid)

    if cutting_height >= M:
        if max_meter < mid:
            max_meter = mid
        low = mid + 1
    elif cutting_height < M:
        high = mid - 1
    else:
        max_meter = mid
        break

print(max_meter)
