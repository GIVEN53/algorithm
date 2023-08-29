from sys import stdin


def binary_search(start, end):
    while start <= end:
        limit = (start + end) // 2
        total_budget = 0
        for b in budget:
            total_budget += b if b < limit else limit

        if total_budget <= m:
            start = limit + 1
        else:
            end = limit - 1
    return end


n = int(stdin.readline())
budget = list(map(int, stdin.readline().split()))
m = int(stdin.readline())

budget.sort()
start, end = 1, budget[-1]
print(binary_search(start, end))

##########################
#    memory: 32276KB     #
#    time:   48ms        #
##########################
