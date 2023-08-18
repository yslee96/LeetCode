class Solution:
    def minSteps(self, n: int) -> int:
        dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        dp[1][0] = 0
        dp[1][1] = 1
        for i in range(1, n+1):
            for j in range(n):
                if i+j <= n:
                    dp[i+j][j] = min(dp[i+j][j], dp[i][j] + 1)
                if i*2 <=n:
                    dp[2*i][i] = min(dp[2*i][i], dp[i][j] + 2)

        return min(dp[n])
         
            