class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_num = 0
        
        @cache
        def maxPoints(num):
            if num==0:
                return 0
            if num==1:
                return points[1]
            return max(maxPoints(num-1), maxPoints(num-2) + points[num])
        
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)
        return maxPoints(max_num)