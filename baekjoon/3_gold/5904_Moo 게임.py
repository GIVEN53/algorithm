from sys import stdin


def rec(moo, mid, n):
    prev_moo = (moo - mid) // 2
    if n <= prev_moo:
        rec(prev_moo, mid - 1, n)
    elif n > prev_moo + mid:
        rec(prev_moo, mid - 1, n - prev_moo - mid)
    else:
        print('m' if n - prev_moo == 1 else 'o')


n = int(stdin.readline())
moo, k = 3, 0
while moo < n:
    k += 1
    moo += moo + k + 3

rec(moo, k + 3, n)
