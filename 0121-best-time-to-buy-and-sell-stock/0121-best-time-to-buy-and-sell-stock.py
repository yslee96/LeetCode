class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = int(1e9)
        max_profit = 0

        for i in range(len(prices)):
            min_value = min(min_value, prices[i])
            max_profit = max(max_profit, prices[i] - min_value)

        return max_profit