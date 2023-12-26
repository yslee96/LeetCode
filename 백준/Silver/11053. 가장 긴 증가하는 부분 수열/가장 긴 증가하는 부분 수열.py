import sys
from bisect import bisect_left
input = sys.stdin.readline
size = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]
for num in nums[1:]:
    if dp[-1] < num:
        dp.append(num)
    else:
        idx = bisect_left(dp, num)
        dp[idx] = num
print(len(dp))