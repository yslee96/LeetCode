import sys
from collections import deque
input = sys.stdin.readline
board_size = int(input())
board = [list(map(int, input().split())) for _ in range(board_size)]

def shark_move(board, board_size, shark_size, row, col):
    possible_fish_info = []
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    visited[row][col] = True
    q = deque()
    q.append([row, col, 0])

    while q:
        cur_row, cur_col, cur_dist = q.popleft()
        if board[cur_row][cur_col] > 0 and board[cur_row][cur_col]!=9 and board[cur_row][cur_col] < shark_size:
            possible_fish_info.append([cur_dist, cur_row, cur_col])
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            n_row, n_col = cur_row + dr, cur_col + dc
            if n_row < 0 or n_row >= board_size  or n_col < 0 or n_col >= board_size: continue
            if visited[n_row][n_col]: continue
            if board[n_row][n_col] <= shark_size:
                visited[n_row][n_col] = True
                q.append([n_row, n_col, cur_dist+1])

        
    return possible_fish_info

def select_fish(fishes):
    fishes.sort()
    return fishes[0]

shark_row, shark_col = -1, -1
for i in range(board_size):
    for j in range(board_size):
        if board[i][j] == 9:
            shark_row = i
            shark_col = j

shark_size = 2
time_cnt = 0
eat_cnt = 0     
while True:
    possible_fish_info = shark_move(board, board_size, shark_size, shark_row, shark_col)
    if not possible_fish_info:
        break
    dist , fish_row, fish_col = select_fish(possible_fish_info)
    if board[shark_row][shark_col] == 9:
        board[shark_row][shark_col] = 0 
    shark_row, shark_col = fish_row, fish_col
    
    fish_size = board[fish_row][fish_col]    
    if fish_size < shark_size:
        board[fish_row][fish_col] = 9
        eat_cnt +=1

    if eat_cnt == shark_size:
        shark_size +=1
        eat_cnt = 0
        
    time_cnt += dist
print(time_cnt)