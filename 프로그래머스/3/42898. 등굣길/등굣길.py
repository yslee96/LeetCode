def solution(m, n, puddles):
    max_row, max_col = n, m
    dp = [[0 for _ in range(max_col+1)] for _ in range(max_row+1)]
    is_puddle = [[False for _ in range(max_col+1)] for _ in range(max_row+1)]
    for col,row in puddles:
        is_puddle[row][col] = True
    dp[1][1] = 1
    for i in range(1,max_row+1):
        for j in range(1,max_col+1):
            if is_puddle[i][j]:
                continue
        
            dp[i][j] += dp[i-1][j] if not is_puddle[i-1][j] else 0
            dp[i][j] += dp[i][j-1] if not is_puddle[i][j-1] else 0
            dp[i][j] %= 1000000007
    return dp[max_row][max_col]