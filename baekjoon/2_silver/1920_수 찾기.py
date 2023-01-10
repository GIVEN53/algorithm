from sys import stdin


# 1
def binary_search(num, low, high):
    if low > high:
        return 0

    mid = (low + high) // 2
    if A[mid] == num:
        return 1
    if A[mid] > i:
        return binary_search(num, low, mid - 1)
    if A[mid] < i:
        return binary_search(num, mid + 1, high)


N = int(stdin.readline())
A = sorted(map(int, stdin.readline().split()))

M = stdin.readline()
nums = map(int, stdin.readline().split())

for i in nums:
    print(binary_search(i, 0, N - 1))


# 2
N = stdin.readline()
A = set(stdin.readline().split())

M = stdin.readline()
nums = stdin.readline().split()

for i in nums:
    print(1 if i in A else 0)
