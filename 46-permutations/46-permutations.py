class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elem = []
        
        def dfs(elem):
            if len(elem) == 0:
                results.append(prev_elem[:])
            for e in elem:
                next_elem = elem[:]
                next_elem.remove(e)
                
                prev_elem.append(e)
                dfs(next_elem)
                prev_elem.pop()
            
        dfs(nums)
        return results
                
            