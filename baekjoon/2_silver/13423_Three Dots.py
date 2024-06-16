from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    dots = sorted(map(int, stdin.readline().split()))
    dots_set = set(dots)

    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            third = dots[j] * 2 - dots[i]
            if third in dots_set:
                ans += 1

    print(ans)
