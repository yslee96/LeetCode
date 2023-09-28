class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        inNums1 = defaultdict(lambda: False)
        inNums2 = defaultdict(lambda: False)
        answer = [set(),set()]
        for num in nums1:
            inNums1[num] = True

        for num in nums2:
            inNums2[num] = True
            if not inNums1[num]:
                answer[1].add(num)

        for num in nums1:
            if not inNums2[num]:
                answer[0].add(num)

        answer = [list(s) for s in answer]
        return answer

        