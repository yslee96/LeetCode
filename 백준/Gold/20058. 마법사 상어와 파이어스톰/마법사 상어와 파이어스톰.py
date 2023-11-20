import sys
from collections import deque
input = sys.stdin.readline
size, num_storms = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(2**size)]
levels = list(map(int,input().split()))

#hard
def rotate(board, level):
    tmp = [[0]*(2**size) for _ in range(2**size)]
    for y in range(0,2**size,2**level):
        for x in range(0,2**size,2**level):
            for i in range(2**level):
                for j in range(2**level):
                    tmp[y+j][x+(2**level)-i-1] = board[y+i][x+j]                 
    board = tmp
    return board

def melt_ice(board):
    to_melt = []
    for row in range(2**size):
        for col in range(2**size):
            cnt = 0
            for offset in [(-1,0),(1,0),(0,-1),(0,1)]:
                t_row = row+offset[0]
                t_col = col+offset[1]
                if 0<=t_row<2**size and 0<=t_col<2**size and board[t_row][t_col]:
                    cnt+=1
            if cnt<3 and board[row][col]!=0:
                to_melt.append([row,col])
    
    for row, col in to_melt:
        board[row][col]-=1
        
    return board 

def bfs(board):
    visited = [[0]*(2**size) for _ in range(2**size)]
    max_cnt = 0
    ice_sum = 0
    for i in range(2**size):
        for j in range(2**size):
            if board[i][j] and not visited[i][j]:
                q = deque()
                q.append([i,j])
                visited[i][j] = 1
                cnt = 0
                while q:
                    row, col = q.popleft()
                    ice_sum += board[row][col]
                    cnt+=1
                    for offset in [(-1,0),(1,0),(0,-1),(0,1)]:
                        n_row, n_col = row+offset[0], col+offset[1]
                        if n_row < 0 or n_row>=2**size or n_col<0 or n_col>=2**size: continue
                        if visited[n_row][n_col]: continue
                        if board[n_row][n_col]:
                            q.append([n_row,n_col])
                            visited[n_row][n_col]=1
                max_cnt = max(cnt, max_cnt)
    return ice_sum, max_cnt

for level in levels:
    board = rotate(board, level)
    board = melt_ice(board)
print(*bfs(board), sep='\n')