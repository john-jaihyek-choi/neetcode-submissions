class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, lowest_price = 0, prices[0]
        l, r = 0, 1
        profit = 0
        
        while(r < len(prices)):
            if prices[r] <= lowest_price:
                lowest_price = prices[r]
                profit = 0
                
                l = r
                r = l + 1
            else:
                profit += prices[r] - prices[r-1]
                r += 1

            max_profit = max(max_profit, profit)

        return max_profit