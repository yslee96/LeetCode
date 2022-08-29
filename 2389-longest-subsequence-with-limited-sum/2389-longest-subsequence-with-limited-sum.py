class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:   
        nums.sort()
        acc_sums = [0 for _ in range(len(nums))]
        answers = []
        acc_sums[0] = nums[0]
        for i in range(1,len(nums)):
            acc_sums[i] = acc_sums[i-1]+nums[i]
        for query in queries:
            answers.append(bisect_right(acc_sums, query))
        return answers