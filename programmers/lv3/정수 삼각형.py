def dfs(h, x, triangle):
    global dp

    if dp[h][x]:
        return dp[h][x]

    for i in range(-1, 1):
        if x + i < 0 or x + i > h - 1:
            continue
        dp[h][x] = max(dp[h][x], dfs(h - 1, x + i, triangle) + triangle[h][x])
    return dp[h][x]


def solution(triangle):
    global dp

    height = len(triangle)
    dp = [[0] * i for i in range(1, height + 1)]
    dp[0][0] = triangle[0][0]
    ans = 0   
    for i in range(height):
        ans = max(ans, dfs(height - 1, i, triangle))    
    return ans