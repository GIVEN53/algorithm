from sys import stdin


def dfs(n, depth, visited, card_sum):
    global card, max_sum

    if n == depth:
        if max_sum < card_sum and M >= card_sum:
            max_sum = card_sum
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n, depth + 1, visited, card_sum + card[i])
            visited[i] = False


N, M = map(int, stdin.readline().split())
card = list(map(int, stdin.readline().split()))
max_sum = 0
dfs(3, 0, [False] * N, 0)

print(max_sum)
