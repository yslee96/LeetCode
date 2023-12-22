import sys
input = sys.stdin.readline
test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    dp = [[0 for _ in range(size+1)] for _ in range(2)]
    stickers = [[0] + list(map(int, input().split())) for _ in range(2)]
    for i in range(1, size+1):
        max_previous = max(dp[0][i-1], dp[1][i-1])
        dp[0][i] = max(dp[1][i-1] + stickers[0][i], max_previous)
        dp[1][i] = max(dp[0][i-1] + stickers[1][i], max_previous)
    print(max(dp[0][size], dp[1][size]))