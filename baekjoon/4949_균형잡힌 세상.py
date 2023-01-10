from sys import stdin
import re

while True:
    s = stdin.readline().rstrip()
    if s == '.':
        break
    s = re.sub("[a-zA-Z\.\s]", '', s)

    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif (stack[-1] == '[' and i == ']') or (stack[-1] == '(' and i == ')'):
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        print("yes")
    else:
        print("no")
