class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rep = [i for i in range(len(isConnected))]
        def find_rep(num):
            if(rep[num]==num):
                return num
            
            rep[num] = find_rep(rep[num])
            return rep[num]

        def is_same_set(num1, num2):
            return find_rep(num1) == find_rep(num2)

        def union_set(num1, num2):
            rep[find_rep(num2)] = rep[find_rep(num1)]
        
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i!=j and isConnected[i][j] and not is_same_set(i,j):
                    union_set(i,j)
        
        ans = 0
        for i in range(len(isConnected)):
            if rep[i] == i:
                ans+=1
        return ans
