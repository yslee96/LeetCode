class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(price, min_price)
            profit = max(price - min_price, profit)
        
        return profit