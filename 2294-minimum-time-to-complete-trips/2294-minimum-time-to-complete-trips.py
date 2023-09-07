class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, 10**15
        while left+1 < right:
            mid = (left+right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid
            else:
                left = mid
        return left+1