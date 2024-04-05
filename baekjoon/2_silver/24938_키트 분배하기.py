from sys import stdin

n = int(stdin.readline())
kit = list(map(int, stdin.readline().split()))
kit_cnt = sum(kit) // n
res = 0

for i in range(n - 1):
    need_kit = kit_cnt - kit[i]
    kit[i + 1] -= need_kit
    res += abs(need_kit)
print(res)
