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
            2. Dynamic Programming:
                - initialize a cache array with size len(cost) 
                - recurse i + 1 step and i + 2 step
                    - base case: i >= 0
                    - if cache[i] exists:
                        - use cached value without recursing
                    - else:
                        - return cost[i] + min(recurse(i+1), recurse(i+2))
            3. Dynamic Programming Space Optimized:
                - directly mutate cost array
                    - since every i'th space depends on i + 1 step and i + 2 steps
                        - I can start mutating the array from the end of the list
                            - ex) complete i + 2 steps, then i + 1 steps, then i
                    - at each step, make locally optimal scenario:
                        - setting each cost[i] to minimum of it's i + 1 or i + 2 sum value
        """
        # DP space optimized:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

        # # DP:
        # cache = [None] * len(cost)
        
        # def dfs(i: int) -> int:
        #     if i >= len(cost):
        #         return 0
        #     elif cache[i]:
        #         return cache[i]
        #     cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return cache[i]

        # return min(dfs(0), dfs(1))


        # # Basic Recursion:
        # if len(cost) <= 2:
        #     return min(cost)

        # def dfs(i: int) -> int:
        #     if i >= len(cost):
        #         return 0
        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))


        # return min(dfs(0), dfs(1))