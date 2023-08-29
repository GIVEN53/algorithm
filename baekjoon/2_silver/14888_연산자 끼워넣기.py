def dfs(idx, num):
    global add, sub, mul, div, result

    if idx == N:
        result.append(num)
        return

    if add > 0:
        add -= 1
        dfs(idx + 1, num + numbers[idx])
        add += 1

    if sub > 0:
        sub -= 1
        dfs(idx + 1, num - numbers[idx])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(idx + 1, num * numbers[idx])
        mul += 1

    if div > 0:
        div -= 1
        dfs(idx + 1, int(num / numbers[idx]))
        div += 1


N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
result = []

dfs(1, numbers[0])
print(max(result))
print(min(result))


# 2
from sys import stdin


def dfs(res, idx):
    global max_res, min_res

    if idx == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:
                dfs(res + nums[idx], idx + 1)
            elif i == 1:
                dfs(res - nums[idx], idx + 1)
            elif i == 2:
                dfs(res * nums[idx], idx + 1)
            else:
                dfs(int(res / nums[idx]), idx + 1)
            operators[i] += 1


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
operators = list(map(int, stdin.readline().split()))

max_res = int(-1e9)
min_res = int(1e9)
dfs(nums[0], 1)

print(max_res)
print(min_res)

##########################
#    memory: 31256KB     #
#    time:   76ms        #
##########################
