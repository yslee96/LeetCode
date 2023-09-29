class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        options = list(product([i for i in range(n)],repeat=2))
        answer = 0
        for option in options:
            row, col = option
            equal = True
            for i in range(n):
                if grid[row][i] != grid[i][col]:
                    equal = False
                    break
            if equal:
                answer +=1
        
        return answer
        