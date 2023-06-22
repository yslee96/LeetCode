class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        num_houses = len(costs)
        num_colors = len(costs[0])
        dp = [[float('inf') for _ in range(num_colors)] for _ in range(num_houses)]
        for i in range(num_colors):
            dp[0][i] = costs[0][i]
            
        for i in range(1, num_houses):
            for j in range(num_colors):
                for k in range(num_colors):
                    if j == k: continue
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + costs[i][j])
        
        return min(dp[num_houses-1])