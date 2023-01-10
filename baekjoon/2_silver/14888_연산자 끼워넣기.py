def dfs(idx, num):
    global add, sub, mul, div, result

    if idx == N:
        result.append(num)
        return

    if add > 0:
        add -= 1
        dfs(idx+1, num + numbers[idx])
        add += 1

    if sub > 0:
        sub -= 1
        dfs(idx+1, num - numbers[idx])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(idx+1, num * numbers[idx])
        mul += 1

    if div > 0:
        div -= 1
        dfs(idx+1, int(num / numbers[idx]))
        div += 1


N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
result = []

dfs(1, numbers[0])
print(max(result))
print(min(result))
