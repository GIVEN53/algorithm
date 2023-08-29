from sys import stdin


def dfs(i, record):
    global max_record

    if i == 10:
        max_record = max(max_record, record)
        return
    elif record + 40 * (10 - i) < max_record:
        return

    now_dice = dices[i]
    for k in range(4):
        if arrived[k]:
            continue

        tmp = [players[k][0], players[k][1]]
        r, c = players[k][0], players[k][1] + now_dice
        if len(board[r]) - 1 < c:
            players[k][0], players[k][1] = r, c
            arrived[k] = True
            dfs(i + 1, record)
            arrived[k] = False
            players[k][0], players[k][1] = tmp
            continue

        if board[r][c] == 40:
            r, c = 4, 0
        elif r == 0 and board[r][c] % 10 == 0:
            r, c = board[r][c] // 10, 0
        elif 0 < r < 4 and board[r][c] % 5 == 0:
            r, c = 5, board[r][c] // 5 - 5

        if [r, c] not in players:
            players[k][0], players[k][1] = r, c
            dfs(i + 1, record + board[r][c])
            players[k][0], players[k][1] = tmp


board = [[i for i in range(0, 41, 2)]]
board.append([10, 13, 16, 19, 25, 30, 35, 40])
board.append([20, 22, 24, 25, 30, 35, 40])
board.append([30, 28, 27, 26, 25, 30, 35, 40])
board.append([40])
board.append([25, 30, 35, 40])

dices = list(map(int, stdin.readline().split()))
players = [[0, 0] for _ in range(4)]
arrived = [False] * 4
max_record = 0
dfs(0, 0)

print(max_record)

##########################
#    memory: 31256KB     #
#    time:   72ms        #
##########################
