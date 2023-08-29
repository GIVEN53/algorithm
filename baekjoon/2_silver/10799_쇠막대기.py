from sys import stdin

bracket = stdin.readline().rstrip()

stack = 0
bar_cnt = 0
for b in bracket.replace("()", "|"):
    if b == "(":
        stack += 1
    elif b == ")":
        stack -= 1
        bar_cnt += 1
    else:
        bar_cnt += stack

print(bar_cnt)

##########################
#    memory: 31388KB     #
#    time:   56ms        #
##########################
