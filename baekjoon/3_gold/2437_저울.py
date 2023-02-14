from sys import stdin

n = int(stdin.readline())
scale = sorted(map(int, stdin.readline().split()))

weight = 1
for i in range(n):
    if weight < scale[i]:
        break
    weight += scale[i]

print(weight)
