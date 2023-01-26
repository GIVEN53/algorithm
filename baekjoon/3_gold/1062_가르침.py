from itertools import combinations
from sys import stdin

n, k = map(int, stdin.readline().split())
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    k -= 5
    no_learned = set()
    words = []
    for _ in range(n):
        w = 0
        for i in set(stdin.readline().rstrip()) - {'a', 'c', 'i', 'n', 't'}:
            bit = 1 << ord(i) - 97
            w |= bit
            no_learned.add(bit)
        words.append(w)

    if len(no_learned) < k:
        print(n)
    else:
        ans = 0
        for comb in combinations(no_learned, k):
            tmp = 0
            for i in comb:
                tmp |= i

            cnt = 0
            for word in words:
                if word & tmp == word:
                    cnt += 1
            ans = max(ans, cnt)
        print(ans)
