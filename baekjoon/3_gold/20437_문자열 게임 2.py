from sys import stdin


def play():
    min_len, max_len = 1e9, 0
    for alpha in alphabet:
        if len(alpha) < k:
            continue
        for i in range(len(alpha) - k + 1):
            length = alpha[i + k - 1] - alpha[i] + 1
            if length < min_len:
                min_len = length
            if length > max_len:
                max_len = length
    if max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)


t = int(stdin.readline())
for _ in range(t):
    w, k = stdin.readline().rstrip(), int(stdin.readline())
    alphabet = [[] for _ in range(26)]
    for j, word in enumerate(w):
        i = ord(word) - 97
        alphabet[i].append(j)
    play()

##########################
#    memory: 31256KB     #
#    time:   200ms       #
##########################
