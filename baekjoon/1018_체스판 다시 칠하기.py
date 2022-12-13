import sys

N, M = map(int, input().split())
chess = []
for _ in range(N):
    chess.append(sys.stdin.readline().rstrip())

result = []
for i in range(N-7):
    for j in range(M-7):
        B_count = 0
        W_count = 0

        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row+col) % 2 == 0:
                    if chess[row][col] != 'B':
                        B_count += 1
                    if chess[row][col] != 'W':
                        W_count += 1
                else:
                    if chess[row][col] != 'B':
                        W_count += 1
                    if chess[row][col] != 'W':
                        B_count += 1
        result.append(min(B_count, W_count))

print(min(result))
