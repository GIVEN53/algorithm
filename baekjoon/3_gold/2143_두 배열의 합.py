from sys import stdin

t = int(stdin.readline())
n = int(stdin.readline())
arr_1 = [*map(int, stdin.readline().split())]
m = int(stdin.readline())
arr_2 = [*map(int, stdin.readline().split())]

sub_sum = {}
for i in range(n):
    k = 0
    for j in range(i, n):
        k += arr_1[j]
        sub_sum[k] = sub_sum.get(k, 0) + 1

ans = 0
for i in range(m):
    k = 0
    for j in range(i, m):
        k += arr_2[j]
        if t - k in sub_sum:
            ans += sub_sum[t - k]

print(ans)

##########################
#    memory: 73244KB     #
#    time:   348ms       #
##########################
