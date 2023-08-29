from sys import stdin

h, w = map(int, stdin.readline().split())
blocks = list(map(int, stdin.readline().split()))

res = 0
for i in range(1, w - 1):
    left = max(blocks[:i])
    right = max(blocks[i + 1 :])
    max_height = min(left, right)
    if max_height > blocks[i]:
        res += max_height - blocks[i]

print(res)

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################
