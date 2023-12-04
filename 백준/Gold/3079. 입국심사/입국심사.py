import sys
input = sys.stdin.readline
num_gates, num_friends = map(int, input().split())
durations = [int(input()) for _ in range(num_gates)]
lo, hi = 0, int(1e20+1)

def check(k):
    pass_sum = sum([k//duration for duration in durations])
    return pass_sum >= num_friends

while lo +1 < hi:
    mid = (lo+hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid
        
print(hi)