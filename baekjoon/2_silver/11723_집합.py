from sys import stdin

m = int(stdin.readline())
board = [0] * 20
all = [1] * 20
empty = [0] * 20

for _ in range(m):
    command = stdin.readline().split()

    if command[0] != 'all' and command[0] != 'empty':
        num = int(command[1]) - 1
        if command[0] == 'add':
            board[num] = 1
        elif command[0] == 'remove':
            board[num] = 0
        elif command[0] == 'check':
            print(board[num])
        else:
            board[num] = 0 if board[num] else 1
    else:
        board[:] = all if command[0] == 'all' else empty
