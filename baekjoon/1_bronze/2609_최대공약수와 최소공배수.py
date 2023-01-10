from sys import stdin


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


a, b = map(int, stdin.readline().split())

gcd = (gcd(a, b))
print(gcd)
print(int(a * b / gcd))
