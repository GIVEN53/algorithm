from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    H, W, N = map(int, stdin.readline().split())
    floor = H if N % H == 0 else N % H
    ho = N // H if N % H == 0 else N // H + 1
    print(floor * 100 + ho)
