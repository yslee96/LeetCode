class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n , m = len(word1), len(word2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        def min_edit_distance(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            
            if dp[i][j]!=-1:
                return dp[i][j]

            ret = 0
            if word1[i-1] == word2[j-1]:
                ret = min_edit_distance(i-1,j-1)
            else:
                #insert
                insert_dist = min_edit_distance(i, j-1)
                #replace
                replace_dist = min_edit_distance(i-1, j-1)
                #delete
                delete_dist = min_edit_distance(i-1, j)
                ret = min(insert_dist, min(replace_dist, delete_dist)) + 1
            
            dp[i][j] = ret
            return dp[i][j]
        
        return min_edit_distance(n, m)

        




        