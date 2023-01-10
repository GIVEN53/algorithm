from sys import stdin

for _ in range(int(stdin.readline())):
    ps = stdin.readline().rstrip()
    stack = []
    for i in ps:
        if i == ')' and not stack:
            stack.append(i)
            break

        if i == '(' or not stack:
            stack.append(i)
        elif stack[-1] == '(' and i == ')':
            stack.pop()

    if stack:
        print('NO')
    else:
        print('YES')
