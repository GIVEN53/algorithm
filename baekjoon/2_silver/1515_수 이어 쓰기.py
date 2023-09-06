from sys import stdin

numbers = stdin.readline().rstrip()
N = 0
i = 0
flag = True
while flag:
    N += 1
    for num in str(N):
        if numbers[i] == num:
            i += 1
        if i == len(numbers):
            flag = False
            break

print(N)

##########################
#    memory: 31256KB     #
#    time:   68ms        #
##########################
