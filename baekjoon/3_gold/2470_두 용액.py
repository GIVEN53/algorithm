# 1 binary search (284 ms)
from sys import stdin


def binary_search(low, high, target):
    while low + 1 < high:
        mid = (low + high) // 2
        if -target <= arr[mid]:
            high = mid
        else:
            low = mid

    if abs(arr[low] + target) < abs(arr[high] + target):
        return arr[low]
    return arr[high]


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

a, b = arr[0], arr[-1]
min_zero = abs(a + b)
for i in range(n - 1):
    target = arr[i]
    other = binary_search(i + 1, n - 1, target)
    if min_zero > abs(target + other):
        a, b = target, other
        min_zero = abs(a + b)
    if min_zero == 0:
        break

print(a, b)


# 2 two pointer (116 ms)
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

start, end = 0, n - 1
min_zero = abs(arr[start] + arr[end])
a, b = start, end
while start < end:
    tot = arr[start] + arr[end]
    if abs(tot) < min_zero:
        min_zero = abs(tot)
        a, b = start, end
    if tot == 0:
        break
    if tot > 0:
        end -= 1
    else:
        start += 1

print(arr[a], arr[b])
