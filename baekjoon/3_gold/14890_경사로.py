from sys import stdin


def can_move(road):
    slope = [False] * N

    i = 1
    while i < N:
        if abs(road[i - 1] - road[i]) > 1:
            return False

        if road[i - 1] > road[i]:
            for j in range(i, i + L):
                if j >= N or road[j] != road[i]:
                    return False
                slope[j] = True
            i += L
        elif road[i - 1] < road[i]:
            if slope[i - L]:
                return False
            for j in range(i - L, i - 1):
                if j < 0 or road[j] != road[i - 1]:
                    return False
            i += 1
        else:
            i += 1

    return True


N, L = map(int, stdin.readline().split())
row_board = [list(map(int, stdin.readline().split())) for _ in range(N)]
col_board = list(zip(*row_board))

cnt = 0
for i in range(N):
    if can_move(row_board[i]):
        cnt += 1
    if can_move(col_board[i]):
        cnt += 1

print(cnt)

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################
