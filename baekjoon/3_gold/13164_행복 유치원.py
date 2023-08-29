from sys import stdin

n, k = map(int, stdin.readline().split())
member = list(map(int, stdin.readline().split()))

differences = [member[i + 1] - member[i] for i in range(n - 1)]
differences.sort()
print(sum(differences[: n - k]))

##########################
#    memory: 66736KB     #
#    time:   236ms       #
##########################
