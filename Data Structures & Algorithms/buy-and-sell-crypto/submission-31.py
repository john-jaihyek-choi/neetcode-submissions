class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input:
            # prices: List[int]
                # list of price at ith day
        # output:
            # output: int
        # goal:
            # given list of integers, return the maximum profit one can achieve
                # one can choose to buy at a single day and sell at another
                # one may choose not to make any transaction
        # idea:
            # bruteforce - check every possibility (TC: O(n^2) / SC: O(1)):
                # initialize max_profit at 0
                # iterate on prices (index = i)
                # iterate on prices at i + 1 (index = j)
                    # max_profit = max(max_profit, prices[j] - prices[i])
            # optimization - keeping the current low:
                # initialize a current low value at max(prices)
                # iterate on prices (price = prices[i])
                    # set max_profit to max(max_profit, price - current_low)
                    # set current_low to min(current_low, price)
                # return max_profit
        
        # Bruteforce pseudocode:
            # max_profit = 0
            # for i in range(len(prices)):
                # for j in range(i + 1, len(prices), 1):
                    # max_profit = max(max_profit, prices[j] - prices[i])
            # return max_profit

        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices), 1):
        #         max_profit = max(max_profit, prices[j] - prices[i])

        # return max_profit

        # Optimized pseudocode:
            # current_low = max(prices)
            # max_profit = 0
            # for price in prices:
                # max_profit = max(max_profit, price - current_low)
                # current_low = min(current_low, price)
            # return max_profit

        current_low = max(prices)
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - current_low)
            current_low = min(current_low, price)
        
        return max_profit

