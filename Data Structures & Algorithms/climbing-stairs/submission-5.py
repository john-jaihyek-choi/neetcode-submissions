class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Intuition:
            1. Recursion (Bruteforce):
                - starting at n = 0, take 2 paths - n + 1 and n + 2
                - recursinon base case:
                    - when > n:
                        - return False
                    - when == n:
                        - return True
        """

        def dfs(num: int):
            if num == n:
                return True
            elif num > n:
                return False
            else:
                return dfs(num + 1) + dfs(num + 2)
        
        return dfs(0)