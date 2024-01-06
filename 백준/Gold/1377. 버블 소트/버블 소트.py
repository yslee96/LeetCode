import sys
input = sys.stdin.readline

arr_size = int(input())
arr = [(int(input()), idx) for idx in range(arr_size)]
arr.sort(key=lambda x: x[0])
max_swaped = 0
for cur_idx in range(arr_size):
    _, pre_idx = arr[cur_idx]
    max_swaped = max(max_swaped, pre_idx - cur_idx)
print(max_swaped+1)