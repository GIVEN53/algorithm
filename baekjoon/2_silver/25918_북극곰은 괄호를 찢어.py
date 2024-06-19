from sys import stdin

n = int(stdin.readline())
s = stdin.readline().rstrip()

stack = []
day = 0
for c in s:
    if stack and stack[-1] == "(" and c == ")":
        stack.pop()
    elif stack and stack[-1] == ")" and c == "(":
        stack.pop()
    else:
        stack.append(c)
        day = max(day, len(stack))

if len(stack):
    print(-1)
else:
    print(day)
