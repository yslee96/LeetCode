import sys
input = sys.stdin.readline
num_kids = int(input())
kids = list(map(int, input().split()))
dp = [0 for _ in range(num_kids+1)]
for kid in kids:
    dp[kid] = dp[kid-1] + 1
print(num_kids - max(dp))