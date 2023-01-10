from sys import stdin


def get_operator(nums):
    stack = []
    operator = []
    i = 1

    for num in nums:
        while i <= num:
            stack.append(i)
            operator.append('+')
            i += 1

        top = stack.pop()
        if top != num:
            return "NO"
        operator.append('-')

    return "\n".join(operator)


n = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(n)]

print(get_operator(nums))
