from sys import stdin

n, m = map(int, stdin.readline().split())
staff = list(map(int, stdin.readline().split()))

left = min(staff)
right = min(staff) * m
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for s in staff:
        cnt += mid // s
    if cnt >= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)
