class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = [False for _ in range(len(candies))]
        cur_max = max(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= cur_max:
                results[i] = True
            
        return results
