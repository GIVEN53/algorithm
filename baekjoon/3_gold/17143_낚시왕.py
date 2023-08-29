from sys import stdin


def catch(j):
    for i in range(R):
        if (i, j) in sharks:
            return sharks.pop((i, j))[2]
    return 0


def move():
    tmp_sharks = {}
    for (r, c), (s, d, z) in sharks.items():
        nr, nc, d = get_next_location(r, c, s, d)

        if (nr, nc) in tmp_sharks and tmp_sharks[(nr, nc)][2] > z:
            continue
        tmp_sharks[(nr, nc)] = (s, d, z)

    return tmp_sharks


def get_next_location(r, c, s, d):
    if d < 2:
        if d == 0:
            s += r_cycle - r
        else:
            s += r
        s %= r_cycle
        if s >= R:
            return r_cycle - s, c, 0
        return s, c, 1
    else:
        if d == 3:
            s += c_cycle - c
        else:
            s += c
        s %= c_cycle
        if s >= C:
            return r, c_cycle - s, 3
        return r, s, 2


R, C, M = map(int, stdin.readline().split())
sharks = {}
for _ in range(M):
    r, c, s, d, z = map(int, stdin.readline().split())
    sharks[(r - 1, c - 1)] = (s, d - 1, z)

catch_size = 0
r_cycle = 2 * (R - 1)
c_cycle = 2 * (C - 1)
for j in range(C):
    catch_size += catch(j)
    sharks = move()

print(catch_size)

##########################
#    memory: 35040KB     #
#    time:   556ms       #
##########################
