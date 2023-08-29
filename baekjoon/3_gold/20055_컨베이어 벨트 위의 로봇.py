from sys import stdin
from collections import deque


def rotate_belt():
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    if robot[-1]:
        robot[-1] = False


def move_robot():
    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1] and belt[i + 1] > 0:
            if i + 1 == n - 1:
                robot[i] = False
            else:
                robot[i], robot[i + 1] = False, True
            decrease_durability(i + 1)


def put_robot():
    if not robot[0] and belt[0] > 0:
        robot[0] = True
        decrease_durability(0)


def decrease_durability(idx):
    global durability_zero

    belt[idx] -= 1
    if belt[idx] == 0:
        durability_zero += 1


n, k = map(int, stdin.readline().split())
belt = deque(map(int, stdin.readline().split()))

robot = deque([False] * n)
step, durability_zero = 0, 0
while durability_zero < k:
    rotate_belt()
    move_robot()
    put_robot()
    step += 1

print(step)

##########################
#    memory: 34140KB     #
#    time:   1496ms      #
##########################
