from sys import stdin

k = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(6)]

h, h_idx = 0, 0
w, w_idx = 0, 0
for i in range(6):
    d, length = arr[i]
    if (d == 1 or d == 2) and w < length:
        w = length
        w_idx = i
    elif (d == 3 or d == 4) and h < length:
        h = length
        h_idx = i

sh = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])
sw = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])
print(k * (h * w - sh * sw))

##########################
#    memory: 31256KB     #
#    time:   40ms        #
##########################
