import sys
input = sys.stdin.readline
num_tests, num_groups = map(int, input().split())
scores = list(map(int, input().split()))

def check_groups(scores, min_score_sum):
    partial_sum = 0
    group_cnt = 0
    for score in scores:
        partial_sum += score
        if partial_sum >= min_score_sum:
            partial_sum = 0
            group_cnt +=1
            
    return group_cnt

left, right = 0, sum(scores) + 1            
while left < right:
    mid = (left+right) // 2
    group_cnt = check_groups(scores, mid)
    if group_cnt < num_groups:
        right = mid
    else:
        left = mid+1
print(left-1)
