import sys
input = sys.stdin.readline
num_matrix = int(input())
matrix = [list(map(int,input().split())) for _ in range(num_matrix)]
dp = [[0]*501 for _ in range(501)]
INF = 2**32
for interval in range(1,num_matrix):
    for start in range(num_matrix-interval):
        dp[start][start+interval] = INF
        for cut in range(start, start+interval+1):
            dp[start][start+interval] = min(dp[start][start+interval], dp[start][cut] + dp[cut+1][start+interval] + matrix[start][0] * matrix[cut][1] * matrix[start+interval][1])
print(dp[0][num_matrix-1])