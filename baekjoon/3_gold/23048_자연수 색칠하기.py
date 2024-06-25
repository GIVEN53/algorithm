from sys import stdin

n = int(stdin.readline())
colored = [0] * (n + 1)
colored[1] = 1

color = 1
for x in range(2, n + 1):
    if not colored[x]:
        color += 1
        colored[x::x] = [color] * (n // x)

print(color)
print(*colored)
