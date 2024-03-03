import sys
from collections import Counter
from itertools import combinations
from bisect import bisect_left

input = sys.stdin.readline

num_size = int(input())
nums = list(map(int, input().split()))
counts = Counter(nums)
nums.sort()

options = list(combinations(range(num_size), 2))
good_nums = set()

for idx1, idx2 in options:
    target = nums[idx1] + nums[idx2]
    target_idx = bisect_left(nums, target)

    if target_idx < num_size and nums[target_idx] == target:
        if target_idx != idx1 and target_idx != idx2:
            good_nums.add(target)

result = 0
for good_num in good_nums:
    result += counts[good_num]

print(result)
