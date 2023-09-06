from sys import stdin

e, s, m = map(int, stdin.readline().split())
year = 1
while (year - e) % 15 + (year - s) % 28 + (year - m) % 19 > 0:
    year += 1
print(year)

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################
