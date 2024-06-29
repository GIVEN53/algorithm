from sys import stdin


def upperbound(v, k):  # k보다 큰 v 원소 중 가장 작은 것 찾기
    low, high = -1, len(v) - 1
    while low + 1 < high:
        mid = (low + high) // 2

        if v[mid] > k:
            high = mid
        else:
            low = mid

    return v[high]


s = list(stdin.readline().rstrip())
t = list(stdin.readline().rstrip())

alpha = [[] for _ in range(26)]
for i in range(len(t)):  # t 문자열에서 각 알파벳의 인덱스
    alpha[ord(t[i]) - 97].append(i)

n = 1
now = -1
for c in s:
    next = alpha[ord(c) - 97]
    if not next:  # s 문자열의 알파벳이 t 문자열에 없을 경우
        n = -1
        break

    if next[-1] <= now:  # t를 이어붙어야 할 경우
        n += 1
        now = -1

    now = upperbound(next, now)

print(n)
