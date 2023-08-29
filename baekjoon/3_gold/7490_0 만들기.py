from sys import stdin


def dfs(now, res, tot):
    if now == n + 1:
        if tot == 0:
            print(res)
        return

    if res[-1] == "1":
        dfs(now + 1, res + " " + str(now), tot * 10 + now)
    elif res[-2] != " ":
        operator = res[-2]
        prev = int(res[-1])
        if operator == "+":
            dfs(now + 1, res + " " + str(now), (tot - prev) + (prev * 10 + now))
        else:
            dfs(now + 1, res + " " + str(now), (tot + prev) - (prev * 10 + now))
    dfs(now + 1, res + "+" + str(now), tot + now)
    dfs(now + 1, res + "-" + str(now), tot - now)


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    dfs(2, "1", 1)
    print()

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################
