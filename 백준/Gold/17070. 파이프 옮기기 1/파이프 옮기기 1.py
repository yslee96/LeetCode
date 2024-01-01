import sys
input = sys.stdin.readline

max_size = int(input())
house = [list(map(int, input().split())) for _ in range(max_size)]
dp = [[{} for _ in range(max_size)] for _ in range(max_size)]

def dfs(row, col, dir):
    if row == max_size -1 and col == max_size-1:
        return 1
    
    if dir in dp[row][col]:
        return dp[row][col][dir]
    
    next_stages = []
    #horizon
    if dir != "ver" and col + 1 < max_size and house[row][col+1] == 0:
        next_stages.append([row, col+1, 'hor'])
    
    #vertical
    if dir != "hor" and row + 1 < max_size and house[row+1][col] == 0:
        next_stages.append([row+1, col, 'ver'])
        
    #diagonal
    if row + 1 < max_size and col + 1 < max_size:
        if house[row+1][col+1] == 0 and house[row+1][col] == 0 and house[row][col+1] == 0:
            next_stages.append([row+1, col+1, 'diag'])
    
    for next_row, next_col, next_dir in next_stages:
        if dir in dp[row][col]:
            dp[row][col][dir] += dfs(next_row, next_col, next_dir)
        else:
            dp[row][col][dir] = dfs(next_row, next_col, next_dir)
            
    return dp[row][col][dir] if dir in dp[row][col] else 0
    

start_row, start_col, start_dir = 0, 1, 'hor'
print(dfs(start_row, start_col, start_dir))