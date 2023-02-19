from sys import stdin

n, k = int(stdin.readline()), int(stdin.readline())
sensor = sorted(map(int, stdin.readline().split()))
distance = sorted([sensor[i + 1] - sensor[i] for i in range(n - 1)], reverse=True)

print(sum(distance[k - 1:]))
