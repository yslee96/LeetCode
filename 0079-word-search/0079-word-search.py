class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        def word_searched(row, col, idx):
            if idx == len(word):
                return True
            
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[idx]:
                return False
            
            tmp = board[row][col]
            board[row][col] = '#'
            for i in range(4):
                n_row = row + dx[i]
                n_col = col + dy[i]
                if word_searched(n_row, n_col, idx+1):
                    return True
            
            board[row][col] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if word_searched(i,j,0):
                    return True
        
        return False
        
        