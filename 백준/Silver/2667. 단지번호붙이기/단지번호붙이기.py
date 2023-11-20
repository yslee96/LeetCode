import sys
input = sys.stdin.readline
size = int(input())
board = [ input().rstrip() for _ in range(size)]
visited =[[0 for _ in range(size)] for _ in range(size)]
results = []
def dfs(row, col):
    if row < 0 or row>=size or col<0 or col>=size:
        return 0
    if visited[row][col]:
        return 0
    
    if board[row][col]=='0':
        return 0

    ret= 1
    visited[row][col] = 1
    for n_row, n_col in [(row+1, col), (row-1,col), (row, col+1), (row, col-1)]:
        ret += dfs(n_row, n_col)

    return ret

for i in range(size):
    for j in range(size):
        if board[i][j]=='1' and not visited[i][j]:
            results.append(dfs(i,j))
results.sort()
print(len(results))
for i in range(len(results)):
    print(results[i], end='\n')