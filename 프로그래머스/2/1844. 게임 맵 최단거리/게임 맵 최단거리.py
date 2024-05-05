from collections import deque
def solution(maps):
    answer = 0
    max_row, max_col = len(maps), len(maps[0])
    visited = [[False for _ in range(max_col)] for _ in range(max_row)]
    q = deque([[0,0,1]])
    visited[0][0] = True
    min_dist = -1
    
    while q:
        cur_row, cur_col, cur_dist = q.popleft()
        if cur_row == max_row-1 and cur_col == max_col-1:
            min_dist = cur_dist
            break
        for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
            n_row, n_col = cur_row + dr, cur_col + dc
            if n_row < 0 or n_row >= max_row or n_col < 0 or n_col >= max_col:
                continue
            if visited[n_row][n_col]:
                continue
            if maps[n_row][n_col]:
                q.append([n_row, n_col, cur_dist+1])
                visited[n_row][n_col] = True
                
    return min_dist