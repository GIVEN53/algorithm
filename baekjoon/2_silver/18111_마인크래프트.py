from collections import Counter
from sys import stdin

N, M, B = map(int, stdin.readline().split())
ground = Counter()
for _ in range(N):
    ground += Counter(map(int, stdin.readline().split()))

height = min(ground)
min_time = 2147483647
max_height = 0
while height <= max(ground):
    time = 0
    pop_B, push_B = 0, 0

    for g, cnt in ground.items():
        if g > height:
            pop_B += (g - height) * cnt  # 제거할 블록
        else:
            push_B += (height - g) * cnt  # 놓을 블록

    if pop_B + B >= push_B:
        time = push_B + (pop_B * 2)
        if time <= min_time:
            min_time = time
            max_height = height

    height += 1

print(min_time, max_height)
