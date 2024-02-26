import sys
from itertools import accumulate
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

target_value = int(input())
a_size = int(input())
arr_a = list(map(int, input().split()))
b_size = int(input())
arr_b = list(map(int, input().split()))

acc_a = [0] + list(accumulate(arr_a))
acc_b = [0] + list(accumulate(arr_b))

b_sums = []
for i in range(1, b_size+1):
    for j in range(i):
        b_sum = acc_b[i] - acc_b[j]
        b_sums.append(b_sum)
b_sums.sort()

result = 0
for i in range(1, a_size+1):
    for j in range(i):
        a_sum = acc_a[i] - acc_a[j]
        result += bisect_right(b_sums, target_value - a_sum) - bisect_left(b_sums, target_value - a_sum)
        
print(result)