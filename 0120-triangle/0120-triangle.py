class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float('inf') for _ in range(i+1)] for i in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                if j <= i-1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + triangle[i][j])
                if j-1 >=0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + triangle[i][j])

        return min(dp[n-1])