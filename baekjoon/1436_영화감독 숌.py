N = int(input())
series = 666
cnt = 0

while 1:
    if '666' in str(series):
        cnt += 1
    if cnt == N:
        break
    series += 1

print(series)
