from sys import stdin


def pow(n, k):
    if k == 1:
        return n % c

    tmp = pow(n, k // 2)
    if k % 2 == 1:
        return n * tmp * tmp % c
    else:
        return tmp * tmp % c


a, b, c = map(int, stdin.readline().split())
print(pow(a, b))

##########################
#    memory: 31256KB     #
#    time:   40ms        #
##########################
