class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        cur_idx = 0
        n = len(nums)
        while cur_idx < n:
            max_idx = max(max_idx, cur_idx+nums[cur_idx])
            if max_idx >= n-1:
                return True
            if max_idx < cur_idx+1:
                return False
            cur_idx +=1
        return True