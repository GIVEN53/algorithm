from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

ans = 0
for i in range(1, n):
    ans += abs(arr[i - 1] - arr[i]) ** 2 + abs(arr[i - 1] + arr[i]) ** 2

print(ans)
