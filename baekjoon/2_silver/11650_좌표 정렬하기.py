from sys import stdin

N = int(stdin.readline())
coordinate = [stdin.readline().split() for _ in range(N)]
coordinate.sort(key=lambda x: int(x[1]))
coordinate.sort(key=lambda x: int(x[0]))

for i in coordinate:
    print(' '.join(i))
