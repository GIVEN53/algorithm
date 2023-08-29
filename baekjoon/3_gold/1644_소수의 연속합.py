from sys import stdin


def get_primes(n):
    sieve = [True] * (n + 1)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i) // (2 * i) + 1)
    return [2] + [i for i in range(3, n + 1, 2) if sieve[i]]


n = int(stdin.readline())
primes = get_primes(n)

slow, fast, total, cnt = 0, 0, 0, 0
while fast < len(primes) or slow < len(primes):
    if total < n:
        if fast == len(primes):
            break
        total += primes[fast]
        fast += 1
    elif total > n:
        total -= primes[slow]
        slow += 1
    else:
        cnt += 1
        total -= primes[slow]
        slow += 1

print(cnt)

##########################
#    memory: 77972KB     #
#    time:   372ms       #
##########################
