from sys import stdin

N = int(stdin.readline())

ans = 0
for i in range(max(1, N - len(str(N) * 9)), N):
    M = i + sum(map(int, str(i)))
    if M == N:
        ans = i
        break
print(ans)
