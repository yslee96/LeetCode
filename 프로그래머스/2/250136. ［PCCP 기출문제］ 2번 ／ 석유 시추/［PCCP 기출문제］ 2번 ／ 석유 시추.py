from collections import deque, defaultdict
def solution(land):
    max_row, max_col = len(land), len(land[0])
    visited = [[False for _ in range(max_col)] for _ in range(max_row)]
    oil_cnts = {col : 0 for col in range(max_col)}

    def bfs(s_row, s_col):
        oil_cnt = 0
        left_most, right_most = max_col, s_col
        q = deque([(s_row, s_col)])
        visited[s_row][s_col] = True
        
        while q:
            row, col = q.popleft()
            oil_cnt +=1
            left_most = min(left_most, col)
            right_most = max(right_most, col)
            for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
                n_row, n_col = row + dr, col + dc
                if n_row < 0 or n_row >= max_row or n_col < 0 or n_col >= max_col:
                    continue
                if land[n_row][n_col] and not visited[n_row][n_col]:
                    q.append((n_row, n_col))
                    visited[n_row][n_col] = True
                    
        for col in range(left_most, right_most +1):
            oil_cnts[col] += oil_cnt
    
    for row in range(max_row):
        for col in range(max_col):
            if land[row][col] and not visited[row][col]:
                bfs(row, col)

    return max(oil_cnts.values())