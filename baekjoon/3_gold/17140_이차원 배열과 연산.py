from sys import stdin
from collections import Counter


def sort(array):
    res, max_len = [], 0
    for arr in array:
        counter = Counter(arr)
        counter.pop(0, None)
        row = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        row = list(sum(row, ()))

        if len(row) > 100:
            row = row[:100]

        max_len = max(max_len, len(row))
        res.append(row)

    return fill_zero(max_len, res)


def fill_zero(max_len, res):
    for row in res:
        if len(row) < max_len:
            row.extend([0] * (max_len - len(row)))

    return res


r, c, k = map(int, stdin.readline().split())
array = [list(map(int, stdin.readline().split())) for _ in range(3)]

sec = 0
while sec < 101:
    row_cnt = len(array)
    col_cnt = len(array[0])
    if row_cnt >= r and col_cnt >= c and array[r - 1][c - 1] == k:
        break

    if row_cnt >= col_cnt:
        array = sort(array)
    else:
        res = sort(list(zip(*array)))
        array = list(zip(*res))

    sec += 1

if sec == 101:
    print(-1)
else:
    print(sec)

##########################
#    memory: 34176KB     #
#    time:   76ms        #
##########################
