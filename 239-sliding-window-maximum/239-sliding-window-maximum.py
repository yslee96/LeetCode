import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        for i, v in enumerate(nums):
            while window and nums[window[-1]] < v:
                window.pop()
            window.append(i)
            if window[0] == i-k:
                window.popleft()
            if i>= k-1:
                results.append(nums[window[0]])
        return results