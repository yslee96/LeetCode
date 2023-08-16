class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        matrix_size = len(matrix)
        dp = [[float('inf') for _ in range(matrix_size)] for _ in range(matrix_size)]
        for i in range(matrix_size):
            dp[0][i] = matrix[0][i]
        for i in range(1,matrix_size):
            for j in range(matrix_size):
                for k in [0, 1, -1]:
                    if j+k >= 0 and j+k < matrix_size:
                        dp[i][j] = min(dp[i][j], dp[i-1][j+k] + matrix[i][j])

        return min(dp[matrix_size-1])