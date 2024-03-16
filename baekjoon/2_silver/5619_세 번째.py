from sys import stdin

n = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(n)]
nums.sort()
new_nums = []
for x in nums[:4]:
    for y in nums[:4]:
        if x == y:
            continue
        num = str(x) + str(y)
        new_nums.append(int(num))
new_nums.sort()

print(new_nums[2])
