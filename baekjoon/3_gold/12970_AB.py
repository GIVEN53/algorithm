from sys import stdin

n, k = map(int, stdin.readline().split())
s = ['B'] * n

a_idx, now_idx, now_k = 0, -1, 0
while now_k < k:
    if now_idx > a_idx - 1:
        s[now_idx] = 'B'
        s[now_idx - 1] = 'A'
        now_k += 1
        now_idx -= 1
    else:
        now_idx = n - 1 - a_idx
        if s[now_idx] == 'A':
            break
        else:
            s[now_idx] = 'A'
            a_idx += 1

if now_k == k:
    print(''.join(s))
else:
    print(-1)
