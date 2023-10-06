class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt = 0
        marks = [[0 for _ in range(n)] for _ in range(n)]
        def is_available(cur_col, q_locs):
            cur_row = len(q_locs)
            for i in range(len(q_locs)):
                if cur_col == q_locs[i] or abs(cur_col-q_locs[i]) == cur_row - i:
                    return False
            return True

        def dfs(cur_row, q_locs, marks):
            nonlocal cnt
            if cur_row == n:
                cnt+=1
                return
            for col in range(n):
                if is_available(col, q_locs):
                    q_locs.append(col)
                    dfs(cur_row+1, q_locs, marks)
                    q_locs.pop()

        dfs(0, [], marks)
        return cnt