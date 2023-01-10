from sys import stdin

N = int(stdin.readline())
people = [list(map(int, stdin.readline().split())) for _ in range(N)]

rank = [1] * N
visited = [False] * N
for i in range(N):
    for j in range(N):
        if not visited[j]:
            x = people[i][0]
            y = people[i][1]
            p = people[j][0]
            q = people[j][1]
            if x > p and y > q:
                rank[j] += 1
            elif x < p and y < q:
                rank[i] += 1
    visited[i] = True

print(" ".join(map(str, rank)))
