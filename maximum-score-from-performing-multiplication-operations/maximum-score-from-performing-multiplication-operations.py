class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        @lru_cache(2000)
        def dp(i,left):
            if i == m:
                return 0
            return max(dp(i+1,left+1) + nums[left]*multipliers[i], 
                       dp(i+1, left)+nums[n-(i-left)-1]*multipliers[i])
        return dp(0,0)
            