import sys
from functools import lru_cache
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
size = int(input())
board = [list(map(int, input().split())) for _ in range(size)]
dp = [[0 for _ in range(size)] for _ in range(size)]
def dfs(row, col):
    if dp[row][col]:
        return dp[row][col]
    
    cnt = 1
    for n_row, n_col in [(row-1,col), (row+1,col), (row,col-1), (row, col+1)]:
        if 0<=n_row<size and 0<=n_col<size and board[row][col] < board[n_row][n_col]:
            cnt = max(cnt, dfs(n_row, n_col) + 1)
    
    dp[row][col] = cnt
    return cnt
        
ans = 0
for i in range(size):
    for j in range(size):
        ans = max(ans, dfs(i,j))
print(ans)