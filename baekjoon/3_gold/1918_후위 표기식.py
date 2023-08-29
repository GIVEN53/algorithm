from sys import stdin

infix = stdin.readline().rstrip()
priority = {"*": 2, "/": 2, "+": 1, "-": 1}
stack = []
res = []
for token in infix:
    if 65 <= ord(token) <= 90:
        res.append(token)
    else:
        if token == ")":
            while stack[-1] != "(":
                res.append(stack.pop())
            stack.pop()
        elif token == "(":
            stack.append(token)
        else:
            if stack and stack[-1] != "(" and priority[stack[-1]] >= priority[token]:
                while (
                    stack
                    and stack[-1] != "("
                    and priority[stack[-1]] >= priority[token]
                ):
                    res.append(stack.pop())
            stack.append(token)

while stack:
    res.append(stack.pop())

print("".join(res))

##########################
#    memory: 31256KB     #
#    time:   40ms        #
##########################
