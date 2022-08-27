class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += matrix[i - 1][j]
        
        max_sum = -float('inf')
        for i in range(m):
            for j in range(i, m):
                col_prefix_sums = [0 for _ in range(n)]
                col_prefix_sums[0] = matrix[j][0] - (0 if i - 1 < 0 else matrix[i - 1][0])
                for l in range(1, n):
                    col_prefix_sums[l] += (col_prefix_sums[l - 1] + matrix[j][l] - (0 if i - 1 < 0 else matrix[i - 1][l]))
                max_sum = max(max_sum, self.process_col_prefix_sums(col_prefix_sums, k))
        
        return max_sum
    
    def process_col_prefix_sums(self, col_prefix_sums, k):
        max_sum = -float('inf')
        ordered_list = []
        ordered_list.append(0)
        for prefix_sum in col_prefix_sums:
            target = prefix_sum - k
            idx = bisect_left(ordered_list, target)
            if idx < len(ordered_list):
                max_sum = max(max_sum, prefix_sum - ordered_list[idx])
            insert_idx = bisect_left(ordered_list, prefix_sum)
            ordered_list.insert(insert_idx, prefix_sum)
        return max_sum