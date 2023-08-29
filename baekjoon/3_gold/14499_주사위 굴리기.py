from sys import stdin
from collections import deque


def turn(command):
    global dice

    top, north, east, west, south, bottom = dice
    if command == 1:
        dice = [west, north, top, bottom, south, east]
    elif command == 2:
        dice = [east, north, bottom, top, south, west]
    elif command == 3:
        dice = [south, top, east, west, bottom, north]
    else:
        dice = [north, bottom, east, west, top, south]


def is_out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


n, m, x, y, k = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
commands = deque(map(int, stdin.readline().split()))

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0, 0, 0, 0, 0, 0]
while commands:
    command = commands.popleft()
    nx, ny = x + direction[command - 1][0], y + direction[command - 1][1]
    if is_out_of_range(nx, ny):
        continue

    x, y = nx, ny
    turn(command)

    if maps[x][y] == 0:
        maps[x][y] = dice[5]
    else:
        dice[5] = maps[x][y]
        maps[x][y] = 0

    print(dice[0])

##########################
#    memory: 34216KB     #
#    time:   64ms        #
##########################
