import sys
from collections import deque, defaultdict
input = sys.stdin.readline

horse_move = int(input())
max_col, max_row = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(max_row)]
visited = defaultdict(int)
answer = -1

q = deque()
q.append([0, horse_move, 0, 0])
visited[(horse_move, 0, 0)] = 1 

while q:
    cur_cnt, horse_cnt, cur_row, cur_col = q.popleft()
    
    if cur_row == max_row-1 and cur_col == max_col-1:
        answer = cur_cnt
        break
    
    #상하좌우
    for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
        nxt_row, nxt_col = cur_row + dr, cur_col + dc
        if nxt_row < 0 or nxt_row >= max_row or nxt_col < 0 or nxt_col >= max_col: continue
        if visited[(horse_cnt, nxt_row, nxt_col)]: continue
        if board[nxt_row][nxt_col] == 0:
            q.append([cur_cnt+1, horse_cnt, nxt_row, nxt_col])
            visited[(horse_cnt, nxt_row, nxt_col)] = 1
            
    if horse_cnt == 0:
        continue
    
    # 말 움직임
    for dr, dc in [(-2, -1),(-2, 1),(-1, -2),(-1, 2),(1, -2),(1, 2),(2, -1),(2, 1)]:
        nxt_row, nxt_col = cur_row + dr, cur_col + dc
        if nxt_row < 0 or nxt_row >= max_row or nxt_col < 0 or nxt_col >= max_col: continue
        if visited[(horse_cnt-1, nxt_row, nxt_col)]: continue
        if board[nxt_row][nxt_col] == 0:
            q.append([cur_cnt+1, horse_cnt-1, nxt_row, nxt_col])
            visited[(horse_cnt-1, nxt_row, nxt_col)] = 1

print(answer)