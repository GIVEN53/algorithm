from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
nums.sort()
cnt = 0
for i in range(n):
    target = nums[i]
    s, e = 0, n - 1
    while s < e:
        tot = nums[s] + nums[e]
        if tot < target:
            s += 1
        elif tot > target:
            e -= 1
        else:
            if s == i:
                s += 1
            elif e == i:
                e -= 1
            else:
                cnt += 1
                break

print(cnt)
