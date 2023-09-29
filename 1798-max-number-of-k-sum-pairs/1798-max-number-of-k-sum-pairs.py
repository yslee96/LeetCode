class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        nums = set(nums)
        result = 0
        checked = defaultdict(int)
        for num in nums:
            if num >= k or checked[num]:
                continue
            if k%2 ==0 and num == k // 2:
                result += floor(counts[num]/2)
                checked[k//2] = 1
            else:
                result += min(counts[num], counts[k-num])
                checked[k-num] = 1
        return result

