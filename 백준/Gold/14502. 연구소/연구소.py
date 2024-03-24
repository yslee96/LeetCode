import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
max_row, max_col = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(max_row)]

def measure_safe_zones(walls, max_row, max_col):
    board = [[origin_board[i][j] for j in range(max_col)] for i in range(max_row)]
    for wall in walls:
        w_row, w_col = wall
        board[w_row][w_col] = 1
        
    q = deque()
    for virus in viruses:
        v_row, v_col = virus
        q.append([v_row, v_col])
    
    while q:
        cur_row, cur_col = q.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            n_row, n_col = cur_row + dr, cur_col + dc
            if n_row < 0 or n_row >= max_row or n_col < 0 or n_col >= max_col: continue
            if board[n_row][n_col] == 0:
                board[n_row][n_col] = 2
                q.append([n_row, n_col])
        
    cur_safe_zones = 0
    for i in range(max_row):
        for j in range(max_col):
            if board[i][j] == 0:
                cur_safe_zones +=1
    
    return cur_safe_zones

blanks = []
viruses = []
for i in range(max_row):
    for j in range(max_col):
        if origin_board[i][j] == 0:
            blanks.append((i,j))
        elif origin_board[i][j] == 2:
            viruses.append((i,j))

max_safe_zones = 0
wall_options = list(combinations(blanks, 3))
for option in wall_options:
    max_safe_zones = max(max_safe_zones, measure_safe_zones(option, max_row, max_col))

print(max_safe_zones)