import sys
input = sys.stdin.readline

num_trees, target_len = map(int, input().split())
trees = sorted(list(map(int, input().split())))
lo, hi = 0, int(1e9+1)

def check(k):
    sum_len = 0
    for tree in trees:
        sum_len += max(0, tree - k)
    return sum_len >= target_len

while lo +1 < hi:
    mid = (lo+hi)//2
    if check(mid):
        lo = mid
    else:
        hi = mid
print(lo)