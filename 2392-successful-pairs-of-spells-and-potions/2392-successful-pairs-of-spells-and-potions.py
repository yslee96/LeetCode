class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        answer = []
        n = len(potions)
        potions.sort()
        for spell in spells:
            lo, hi = -1, n
            while lo+1 < hi:
                mid = (lo+hi)//2
                if spell * potions[mid] < success:
                    lo = mid
                else:
                    hi = mid
            answer.append(n-1-lo)
        return answer

        
        