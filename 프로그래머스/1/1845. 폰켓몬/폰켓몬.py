from collections import Counter
def solution(nums):
    return min(len(Counter(nums).keys()), len(nums)//2)
