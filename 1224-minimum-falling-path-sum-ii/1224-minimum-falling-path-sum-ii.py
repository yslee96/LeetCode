class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [ [float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        
        for i in range(1,n):
            for j in range(n):
                for k in range(n):
                    if j == k: continue
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])
        print(dp)
        return min(dp[n-1])