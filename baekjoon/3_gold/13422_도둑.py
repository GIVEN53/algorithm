from sys import stdin

for _ in range(int(stdin.readline())):
    n, m, k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))

    total = sum(arr[:m])
    if n == m:
        print(1 if total < k else 0)
        continue

    ans = 0
    for i in range(n):
        total = total - arr[i] + arr[(i + m) % n]
        if total < k:
            ans += 1

    print(ans)
