import sys
input = sys.stdin.readline

def num_paths(max_row, max_col, must_visit_num):
    pass_row = pass_col = -1
    if must_visit_num != 0:
        pass_row = (must_visit_num-1) // max_col + 1
        pass_col = (must_visit_num-1) % max_col + 1
        
    dp = [[[0,0] for _ in range (max_col+1)] for _ in range(max_row+1)]
    dp[1][1][0] = 1
    
    for row in range(1, max_row+1):
        for col in range(1, max_col+1):
            if row == 1 and col == 1:
                continue
            # move from above
            if row > 1:
                dp[row][col][0] += dp[row-1][col][0]
                dp[row][col][1] += dp[row-1][col][1]
            # move froom left
            if col > 1:
                dp[row][col][0] += dp[row][col-1][0]
                dp[row][col][1] += dp[row][col-1][1]
            if row == pass_row and col == pass_col:
                dp[row][col][1] += dp[row][col][0]
                dp[row][col][0] = 0
    
    return dp[max_row][max_col][1] if must_visit_num !=0 else dp[max_row][max_col][0]

max_row, max_col, must_visit_num  = map(int, input().split())
print(num_paths(max_row, max_col, must_visit_num))