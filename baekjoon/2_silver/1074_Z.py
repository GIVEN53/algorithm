from sys import stdin


def get_rank(N, r, c):
    if N == 0:
        return 0

    return 2 * (r % 2) + (c % 2) + 4 * get_rank(N - 1, r // 2, c // 2)


N, r, c = map(int, stdin.readline().split())
print(get_rank(N, r, c))
