class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            lo, hi = 0, len(arr)
            while lo +1 < hi:
                mid = (lo+hi) // 2
                if arr[mid] <= target:
                    lo = mid
                else:
                    hi = mid
            return lo
        first_integers = [matrix[i][0] for i in range(len(matrix))]
        tmp = binary_search(first_integers, target)
        target_row = matrix[tmp]
        target_idx = binary_search(target_row, target)
        return matrix[tmp][target_idx] == target