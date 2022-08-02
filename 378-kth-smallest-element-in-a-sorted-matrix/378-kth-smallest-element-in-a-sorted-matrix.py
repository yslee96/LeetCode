class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
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