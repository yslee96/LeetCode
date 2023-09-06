class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right = 0, 10**7+1
        while left +1 < right:
            mid = (left+right) // 2
            if sum(math.ceil(d/mid) for d in dist[:-1]) + dist[-1]/mid <= hour:
                right = mid
            else:
                left = mid
        return left+1 if left != 10**7 else -1

                