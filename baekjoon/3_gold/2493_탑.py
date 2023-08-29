from sys import stdin

n = int(stdin.readline())

res = [0] * n
stack = []
for i, height in enumerate(map(int, stdin.readline().split())):
    if stack and stack[-1][0] < height:
        while stack and stack[-1][0] < height:
            stack.pop()
    if stack:
        res[i] = stack[-1][1]

    stack.append((height, i + 1))

print(" ".join(map(str, res)))

##########################
#    memory: 141840KB    #
#    time:   552ms       #
##########################
