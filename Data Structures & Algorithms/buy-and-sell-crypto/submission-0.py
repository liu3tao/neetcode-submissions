class Solution:
    # Just move left bound when the next is smaller, move right bound when the next is larger.
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(p, minPrice)
        return maxProfit
            
            
        