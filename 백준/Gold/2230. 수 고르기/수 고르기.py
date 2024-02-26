import sys
input = sys.stdin.readline
size, target_diff = map(int, input().split())
seq = [int(input()) for _ in range(size)]
seq.sort()

left = right = 0
min_diff = float('inf')
while left <= right and right < size:
    tmp_diff = seq[right] - seq[left]
    if tmp_diff > target_diff:
        if min_diff > tmp_diff:
            min_diff = tmp_diff
        left +=1
    elif tmp_diff == target_diff:
        min_diff = target_diff
        break
    else:
        right+=1
        
print(min_diff)