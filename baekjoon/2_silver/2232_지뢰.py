from sys import stdin

n = int(stdin.readline())
mine = [0] + [int(stdin.readline()) for _ in range(n)] + [0]

for i in range(1, n + 1):
    if mine[i - 1] <= mine[i] and mine[i] >= mine[i + 1]:
        print(i)
