class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Intuition:
            1. Basic recursion
                - 2 unique starting points:
                    - cost[0]
                    - cost[1]
                - recurse i + 1 step and i + 2 step
                    - base case: when i >= len(cost)
                        - return 0
                    - cost[i] + min(recurse(i + 1), recurse(i + 2))
        """

        if len(cost) <= 2:
            return min(cost)

        def dfs(i: int) -> int:
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i + 1), dfs(i + 2))


        return min(dfs(0), dfs(1))