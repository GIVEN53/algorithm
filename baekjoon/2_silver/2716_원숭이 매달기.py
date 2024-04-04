from sys import stdin

for _ in range(int(stdin.readline())):
    vine = stdin.readline().strip()
    depth = 0
    stack = []
    for v in vine:
        if v == "[":
            stack.append(v)
        else:
            depth = max(depth, len(stack))
            stack.pop()
    print(2**depth)
