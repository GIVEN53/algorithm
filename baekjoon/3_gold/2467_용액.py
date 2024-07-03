from sys import stdin


def binary_search(low, high, x):
    while low + 1 < high:
        mid = (low + high) // 2
        if -x <= arr[mid]:
            high = mid
        else:
            low = mid

    if abs(arr[high] + x) < abs(arr[low] + x):
        return arr[high]
    else:
        return arr[low]


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

a, b = arr[0], arr[-1]
min_zero = abs(a + b)
for i in range(n - 1):
    x = arr[i]
    y = binary_search(i + 1, n - 1, x)
    if abs(x + y) < min_zero:
        min_zero = abs(x + y)
        a, b = x, y

    if min_zero == 0:
        break

print(a, b)
