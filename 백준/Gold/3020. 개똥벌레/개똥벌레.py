import sys
from collections import defaultdict
input = sys.stdin.readline
upper, lower = [], []
cave_len, cave_height = map(int, input().split())
for i in range(cave_len):
    if i % 2:
        upper.append(int(input()))
    else:
        lower.append(int(input()))
upper.sort()
lower.sort()

def lower_bound(arr, target):
    lo, hi  = -1, cave_len//2
    while lo+1 < hi:
        mid = (lo+hi) // 2
        if target <= arr[mid]:
            hi = mid
        else:
            lo = mid
    #print("lo, hi:", lo, hi)
    #print(arr)
    #print("cnt:",cave_len//2-(lo+1))
    return cave_len//2 - (lo+1)

min_obstacles = cave_len
obstcale_counts = defaultdict(int) 
for i in range(1,cave_height+1):
    cur_obstacles= lower_bound(lower, i) + lower_bound(upper, cave_height-i+1) 
    #print(i,cur_obstacles)
    obstcale_counts[cur_obstacles]+=1
    min_obstacles = min(min_obstacles, cur_obstacles)
print(min_obstacles, obstcale_counts[min_obstacles])
