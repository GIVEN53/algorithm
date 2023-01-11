from sys import stdin

N = int(stdin.readline())
members = [stdin.readline().split() for _ in range(N)]
members.sort(key=lambda x: int(x[0]))

for i in members:
    print(" ".join(i))
