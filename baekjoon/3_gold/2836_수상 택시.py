from sys import stdin

n, m = map(int, stdin.readline().split())
house = []
for _ in range(n):
    start, end = map(int, stdin.readline().split())
    if start > end:
        house.append((start, end))
house.sort(reverse=True)

total = 0
start, end = house[0]
for s, e in house[1:]:
    if s < end:
        total += start - end
        start, end = s, e
    elif e < end:
        end = e

total += start - end
print(total * 2 + m)

##########################
#    memory: 74320KB     #
#    time:   692ms       #
##########################
