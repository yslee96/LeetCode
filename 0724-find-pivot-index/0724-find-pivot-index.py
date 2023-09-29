class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = [0 for _ in range(n)]
        suffix_sums = [0 for _ in range(n)]

        prefix_sums[0] = nums[0]
        suffix_sums[-1] = nums[-1]

        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i-1] + nums[i]
        for i in range(n-2, -1, -1):
            suffix_sums[i] = suffix_sums[i+1] + nums[i]
        
        pivot_idx = -1
        for i in range(n):
            prefix_sum = prefix_sums[i-1] if i>0 else 0
            suffix_sum = suffix_sums[i+1] if i<n-1 else 0
            if prefix_sum == suffix_sum:
                pivot_idx = i
                break
        return pivot_idx
