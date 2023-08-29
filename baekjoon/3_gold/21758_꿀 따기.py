from sys import stdin


def fly():
    honey_amount = 0
    for i in range(1, n - 1):
        bee_1 = accum_honey[n - 1] - honey[i] - honey[0]
        bee_2 = accum_honey[n - 1] - accum_honey[i]
        honey_amount = max(honey_amount, bee_1 + bee_2)

        bee_1 = accum_honey[i] - honey[0]
        bee_2 = accum_honey[n - 2] - accum_honey[i - 1]
        honey_amount = max(honey_amount, bee_1 + bee_2)

        bee_1 = accum_honey[i - 1]
        bee_2 = accum_honey[n - 2] - honey[i]
        honey_amount = max(honey_amount, bee_1 + bee_2)
    return honey_amount


n = int(stdin.readline())
honey = list(map(int, stdin.readline().split()))
accum_honey = honey[:]
for i in range(1, n):
    accum_honey[i] += accum_honey[i - 1]

print(fly())

##########################
#    memory: 42340KB     #
#    time:   172ms       #
##########################
