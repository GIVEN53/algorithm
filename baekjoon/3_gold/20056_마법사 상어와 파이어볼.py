from sys import stdin


def move() -> dict:
    moved_grid = {}
    for (r, c), fire_balls in grid.items():
        for m, s, d in fire_balls:
            nr = (r + direction[d][0] * s) % N
            nc = (c + direction[d][1] * s) % N

            if (nr, nc) in moved_grid:
                moved_grid[(nr, nc)].append((m, s, d))
            else:
                moved_grid[(nr, nc)] = [(m, s, d)]
    return moved_grid


def add_fire_ball() -> list:
    added_result = []
    for (r, c), fire_balls in grid.items():
        if len(fire_balls) < 2:
            continue
        mass, speed = 0, 0
        odd, even = len(fire_balls), len(fire_balls)
        for m, s, d in fire_balls:
            mass += m
            speed += s

            if d % 2 == 0:
                even -= 1
            else:
                odd -= 1

        grid[(r, c)] = []
        if even != 0 and odd != 0:
            added_result.append(((r, c), mass, speed, [1, 3, 5, 7], len(fire_balls)))
        else:
            added_result.append(((r, c), mass, speed, [0, 2, 4, 6], len(fire_balls)))

    return added_result


def devide_fire_ball(added_result: list):
    for (r, c), mass, speed, new_direction, length in added_result:
        per_mass, per_speed = mass // 5, speed // length
        if per_mass == 0:
            continue
        for d in new_direction:
            grid[(r, c)].append((per_mass, per_speed, d))


def get_total_mass():
    total_mass = 0
    for _, fire_balls in grid.items():
        for m, s, d in fire_balls:
            total_mass += m

    return total_mass


N, M, K = map(int, stdin.readline().split())
grid = {}
for _ in range(M):
    r, c, m, s, d = map(int, stdin.readline().split())
    grid[(r - 1, c - 1)] = [(m, s, d)]

direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
while K:
    K -= 1
    grid = move()
    added_result = add_fire_ball()
    devide_fire_ball(added_result)

print(get_total_mass())

##########################
#    memory: 34324KB     #
#    time:   300ms       #
##########################
