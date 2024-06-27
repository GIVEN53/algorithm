from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

ans = 0
for i in range(n - 1):
    ans = max(ans, min(arr[i], arr[i + 1]))

for i in range(n - 2):
    ans = max(ans, min(arr[i], arr[i + 2]))

print(ans)
