class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #Approach1 : Binary_Search
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l < r:
            m = l + (r - l) // 2
            # print(m)
            # calculate how many numbers are on the left of middle number
            if sum(bisect.bisect_right(row, m) for row in matrix) < k:   

                l = m + 1
            else:
                r = m
        return l
        
        #Approach2 : simple sort
        num_dict = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] in num_dict:
                    num_dict[matrix[i][j]] +=1
                else:
                    num_dict[matrix[i][j]] = 1
        sorted_dict = sorted(num_dict.items())
        cur_cnt = 0
        for key, cnt in sorted_dict:
            cur_cnt += cnt
            if cur_cnt >=k:
                answer = key
                break
                
        return answer
