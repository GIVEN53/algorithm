from sys import stdin

n = int(stdin.readline())
crosswalk = list(map(int, stdin.readline().split()))
left = [0] + list(map(int, stdin.readline().split()))
right = list(map(int, stdin.readline().split())) + [0]

for i in range(1, n):
    left[i] += left[i - 1]
    right[n - i - 1] += right[n - i]

res = 1e11
point = 0
for i in range(n):
    total = left[i] + crosswalk[i] + right[i]
    if total < res:
        res = total
        point = i

print(point + 1, res)
