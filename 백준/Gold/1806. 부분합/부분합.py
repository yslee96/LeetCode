nums, target = map(int, input().split())
seq = list(map(int, input().split()))

tmp_len, cur_sum = 0, 0
right = 0
min_len = float('inf')
for left in range(nums):
    while cur_sum < target and right < nums:
        cur_sum += seq[right]
        right +=1
        tmp_len +=1
    if cur_sum >= target:
        min_len = min(min_len, tmp_len)
    cur_sum -= seq[left]
    tmp_len -=1
print(min_len if min_len!=float('inf') else 0)