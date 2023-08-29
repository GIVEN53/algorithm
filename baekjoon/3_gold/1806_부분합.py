from sys import stdin

n, s = map(int, stdin.readline().split())
seq = [*map(int, stdin.readline().split())]

slow = fast = tot = len = 0
min_len = n + 1
while slow < n:
    if tot < s:
        if fast == n:
            break
        tot += seq[fast]
        fast += 1
        len += 1
    elif tot >= s:
        min_len = min(min_len, len)
        tot -= seq[slow]
        slow += 1
        len -= 1


print(min_len if min_len < n + 1 else 0)

##########################
#    memory: 42340KB     #
#    time:   144ms       #
##########################
