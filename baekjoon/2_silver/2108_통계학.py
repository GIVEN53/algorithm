from sys import stdin


N = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(N)]
nums.sort()

print(round(sum(nums) / N))
print(nums[N // 2])

mode = {}
for i in nums:
    if i in mode:
        mode[i] += 1
    else:
        mode[i] = 1

sorted_mode = dict(sorted(mode.items(), key=lambda x: x[1], reverse=True))

keys = list(sorted_mode.keys())
values = list(sorted_mode.values())
if values.count(values[0]) > 1:
    print(keys[1])
else:
    print(keys[0])

print(nums[-1] - nums[0])
