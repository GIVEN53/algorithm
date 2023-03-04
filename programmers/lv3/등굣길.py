direction = [0, 1]


def dfs(x, y, m, n):
    global board
    
    if board[x][y]:
        return board[x][y]
           
    for i in range(2):
        nx = x + direction[i]
        ny = y + direction[1 - i]
        
        if out_of_range(nx, ny, m, n) or board[nx][ny] == -1:
            continue        
        board[x][y] += dfs(nx, ny, m, n)
    
    return board[x][y]
        
 
def out_of_range(x, y, m, n):
    return x > n - 1 or y > m - 1


def solution(m, n, puddles):
    global board
    
    board = [[0] * m for _ in range(n)]    
    for y, x in puddles:
        board[x - 1][y - 1] = -1
        
    board[n - 1][m - 1] = 1
    dfs(0, 0, m, n)
    return board[0][0] % 1000000007
