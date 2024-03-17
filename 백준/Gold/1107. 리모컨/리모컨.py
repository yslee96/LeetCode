import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
brokens = list(map(int, input().split()))
#candid1
min_count = abs(100 - target)
#candid2
for nums in range(1000001):
    nums = str(nums)    
    for digit in range(len(nums)):
        if int(nums[digit]) in brokens:
            break
        elif digit == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))
print(min_count)