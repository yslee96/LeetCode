import sys
from collections import defaultdict, deque
input = sys.stdin.readline

board_size = int(input())
board = [list(map(int, input().split())) for _ in range(board_size)]

visited = [[0 for _ in range(board_size)] for _ in range(board_size)]
min_bridge_len = float('inf')
land_num = 1


def bfs(row, col, num):
    visited[row][col] = 1
    board[row][col]= num
    q = deque()
    q.append((row, col))
    while q:
        cur_row, cur_col = q.popleft()
        for dr, dc in [(0,1), (0,-1), (-1,0),(1,0)]:
            n_row, n_col = cur_row + dr, cur_col + dc
            if n_row < 0 or n_row>=board_size or n_col < 0 or n_col>=board_size : continue
            if board[n_row][n_col] == 1 and not visited[n_row][n_col] :
                visited[n_row][n_col] = 1
                board[n_row][n_col] = num
                q.append((n_row, n_col))

def build_bridge(row, col, cur_land):
    global min_bridge_len
    is_visited = [[0 for _ in range(board_size)] for _ in range(board_size)]
    q = deque()

    is_visited[row][col] = 1
    q.append((row, col, 0))
    while q:
        cur_row, cur_col, cur_dist = q.popleft()
        
        for dr, dc in [(0,1), (0,-1), (-1,0),(1,0)]:
            n_row, n_col = cur_row + dr, cur_col + dc
            if n_row < 0 or n_row>=board_size or n_col < 0 or n_col>=board_size : continue
            if board[n_row][n_col] == 0 and not is_visited[n_row][n_col] :
                is_visited[n_row][n_col] = 1
                q.append((n_row, n_col, cur_dist+1))  
            if board[n_row][n_col] > 0 and board[n_row][n_col] != cur_land:
                min_bridge_len = min(min_bridge_len, cur_dist)

for i in range(board_size):
    for j in range(board_size):
        if board[i][j] and not visited[i][j]:
            bfs(i,j,land_num)
            land_num+=1

for i in range(board_size):
    for j in range(board_size):
        if board[i][j] != 0:
            is_edge = False
            for dx, dy in [(0,1), (0,-1), (-1,0),(1,0)]:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= board_size or ny < 0 or ny >= board_size: continue
                if board[nx][ny] == 0:
                    is_edge = True
                    break
            if is_edge:
                cur_land = board[i][j]
                build_bridge(i,j, cur_land)

print(min_bridge_len)