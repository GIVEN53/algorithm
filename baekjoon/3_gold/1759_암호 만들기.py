from itertools import combinations
from sys import stdin


# 1
L, C = map(int, stdin.readline().split())
letters = sorted(stdin.readline().split())

vowel = {'a', 'e', 'i', 'o', 'u'}
for comb in combinations(letters, L):
    if set(comb) & vowel and len(set(comb) - vowel) > 1:
        print(''.join(comb))


# 2
def dfs(idx, crypto, vowel_cnt):
    if vowel_cnt > L - 2:
        return

    if len(crypto) == L and vowel_cnt > 0:
        print(crypto)
        return
    
    for i in range(idx, C):
        if letters[i] in vowel:
            dfs(i + 1, crypto + letters[i], vowel_cnt + 1)
        else:
            dfs(i + 1, crypto + letters[i], vowel_cnt)


L, C = map(int, stdin.readline().split())
letters = sorted(stdin.readline().split())

vowel = {'a', 'e', 'i', 'o', 'u'}
dfs(0, '', 0)
