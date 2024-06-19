from sys import stdin

n, m = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

max_end = [0] * n
end = seq[-1]
for i in range(n - 1, -1, -1):
    end = max(end, seq[i])
    max_end[i] = end

ans = -1e9
for i in range(m + 1):
    start = seq[i]
    end = max_end[n - 1 - (m - i)]
    ans = max(ans, end - start)

print(ans)
