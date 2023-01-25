from sys import stdin


N = int(stdin.readline())
coins = []
reverse_coins = []
for _ in range(N):
    i = N - 1
    bit = 0
    for state in stdin.readline().rstrip():
        if state == 'T':
            bit += 1 << i
        i -= 1
    coins.append(bit)
    reverse_coins.append(~bit)

ans = N ** 2
for bit in range(1 << N):
    tmp_coins = []
    for i in range(N):
        if bit & 1 << i:
            tmp_coins.append(coins[i])
        else:
            tmp_coins.append(reverse_coins[i])

    total_t_cnt = 0
    for i in range(N):
        t_cnt = 0
        for coin in tmp_coins:
            if 1 << i & coin:
                t_cnt += 1
        total_t_cnt += min(t_cnt, N - t_cnt)
    ans = min(ans, total_t_cnt)

print(ans)
