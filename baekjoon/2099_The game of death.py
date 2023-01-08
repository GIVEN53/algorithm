import sys


def mul(matrix):
    temp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if matrix[i][j] and matrix[j][k]:
                    temp[i][k] = 1
    return temp


def pow(matrix_point, K):
    if K == 1:
        return matrix_point

    if K % 2 == 0:
        temp = pow(matrix_point, K // 2)
        return mul(temp)
    else:
        temp = pow(matrix_point, K - 1)
        return mul(temp)


N, K, M = map(int, sys.stdin.readline().split())
matrix_point = [[0] * N for _ in range(N)]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    matrix_point[i][a - 1] = matrix_point[i][b - 1] = 1

matrix_pow = pow(matrix_point, K)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print("death" if matrix_pow[a - 1][b - 1] else "life")
