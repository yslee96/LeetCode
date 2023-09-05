class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = defaultdict(lambda:-1)
        def frog_jump(idx, k):
            if idx >= len(stones):
                return False
            if idx == len(stones)-1:
                return True    
            if dp[(idx,k)]!=-1:
                return dp[(idx,k)]
            
            for i in [-1, 0, 1]:
                if idx ==0 and i!=0: continue
                if k+i <=0: continue
                next_pos = stones[idx] + k+i
                next_idx = -1
                for j in range(idx+1, len(stones)):
                    if stones[j] > next_pos: break
                    if stones[j] == next_pos:
                        next_idx = j
                if next_idx!=-1 and frog_jump(next_idx, k+i):
                    dp[(idx,k)] = 1
                    return dp[(idx,k)]

            dp[(idx,k)] = 0
            return dp[(idx,k)]
        return frog_jump(0, 1)
        
        