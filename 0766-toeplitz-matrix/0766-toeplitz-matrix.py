class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        max_row, max_col = len(matrix), len(matrix[0])
        
        
        for i in range(max_col):
            cur_col = i
            for cur_row in range(max_row):
                #print(cur_row, cur_col)
                cur_num = matrix[cur_row][cur_col]
                if cur_row ==0:
                    pre_num = cur_num
                if pre_num != cur_num:
                    return False
                cur_col +=1
                if cur_col == max_col:
                    break
        for i in range(1, max_row):
            cur_row = i
            for cur_col in range(max_col):
                cur_num = matrix[cur_row][cur_col]
                if cur_col ==0:
                    pre_num = cur_num
                if pre_num!=cur_num:
                    return False
                cur_row +=1
                if cur_row == max_row:
                    break
        
        return True

            