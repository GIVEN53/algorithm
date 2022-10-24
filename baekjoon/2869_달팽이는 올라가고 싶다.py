import math


up, down, goal = map(int, input().split())

day = math.ceil((goal-up)/(up-down)) +1
print(day)