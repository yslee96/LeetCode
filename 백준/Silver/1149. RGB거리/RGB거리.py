import sys
input = sys.stdin.readline

num_homes = int(input())
dp = [[0]*3 for _ in range(num_homes)]
for i in range(num_homes):
    costs = list(map(int, input().split()))
    for j in range(3):
        dp[i][j] = costs[j]
for i in range(1, num_homes):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[num_homes-1][0], dp[num_homes-1][1], dp[num_homes-1][2]))