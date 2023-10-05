class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(candidates)
        def find_combis(idx, cur_sum, combis):
            if cur_sum > target:
                return
            if cur_sum == target:
                n_combis = combis[:]
                answer.append(n_combis)
            
            
            for i in range(idx, n):
                combis.append(candidates[i])
                find_combis(i, cur_sum+candidates[i], combis)
                combis.pop()

        find_combis(0, 0, [])
        return answer