class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        zero_cnt = 0
        while idx < len(nums):
            if nums[idx] == 0:
                zero_cnt+=1
                del nums[idx]
            else:
                idx+=1
        for _ in range(zero_cnt):
            nums.append(0)
            
        