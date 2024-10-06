# 1 2중 for문 + binary search -> n^2logn (924ms PyPy3)
from sys import stdin


def binary_search(low, high, target):
    while low + 1 < high:
        mid = (low + high) // 2
        if -target <= arr[mid]:
            high = mid
        else:
            low = mid

    if abs(target + arr[low]) < abs(target + arr[high]):
        return arr[low]
    return arr[high]


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

a = b = c = 0
res = 3e9  # 세 수의 합 최댓값은 30억
flag = 0
for i in range(n - 2):  # 마지막 두 개는 볼 필요없음
    for j in range(i + 1, n - 1):  # 마지막 한 개는 볼 필요없음
        target = arr[i] + arr[j]
        other = binary_search(j + 1, n - 1, target)
        if abs(target + other) < res:
            res = abs(target + other)
            a, b, c = arr[i], arr[j], other
        if res == 0:
            flag = 1
            break
    if flag:
        break

print(a, b, c)


# 2 two pointer (3972ms Python3)
from sys import stdin

n = int(stdin.readline())
arr = sorted(list(map(int, stdin.readline().split())))

a = b = c = 0
res = 3e9
for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        tot = arr[i] + arr[left] + arr[right]
        if abs(tot) < res:
            res = abs(tot)
            a, b, c = arr[i], arr[left], arr[right]

        if tot > 0:
            right -= 1
        else:
            left += 1

print(a, b, c)
