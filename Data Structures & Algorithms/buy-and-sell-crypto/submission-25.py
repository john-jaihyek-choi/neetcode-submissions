class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        lowest = prices[0]
        max_profit = 0

        while r < len(prices):
            if  prices[r] < lowest:
                lowest = prices[r]
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        
        return max_profit