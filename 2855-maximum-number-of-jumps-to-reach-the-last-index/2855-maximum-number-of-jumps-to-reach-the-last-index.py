class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None) 
        def dp(i):
            if i == len(nums) - 1:
                return 0
            res = 0
            f = False
            for j in range(i + 1, len(nums)):
                dj = dp(j)
                if abs(nums[j] - nums[i]) <= target and dj != -1:
                    res = max(res, 1 + dj)
                    f = True
            if not f:
                return -1
            return res
                
        return dp(0)