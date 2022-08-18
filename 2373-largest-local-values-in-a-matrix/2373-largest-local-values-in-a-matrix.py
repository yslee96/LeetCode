class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def getMax(row, col):
            ret = 0
            for i in range(3):
                ret = max(ret, max(grid[row+i][col:col+3]))
            return ret
        ans = [ [0 for _ in range(len(grid)-2)] for _ in range(len(grid)-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                ans[i][j] = getMax(i,j)
        return ans
                
        