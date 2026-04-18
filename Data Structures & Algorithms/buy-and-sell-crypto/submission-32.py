class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Note:
            - max profit?
                - buy at min
                - buy at max
            - len(prices) >= 1:
            - return max profit I can achieve
        Bruteforce:
            - 2 loops to compute every possibility
            - TC: O(n^2) / SC: O(1)
        First-thought Solution (track local min):
            - if len(prices) <= 1, return 0
            - initialize local min (mn) at prices[0]
            - initialize profit at 0
            - iterate on prices starting at first index:
                - compute possible max profit
                    - profit = max(profit, prices[i] - mn)
                - update min
                    - mn = min(mn, prices[i])
            - TC: O(n) / SC: O(1)
        """

        if len(prices) <= 1: return 0

        mn, profit = prices[0], 0
        for p in prices:
            profit = max(profit, p - mn)
            mn = min(mn, p)

        return profit
