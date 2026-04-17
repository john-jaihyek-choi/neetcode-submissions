class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Intuition:
            - Calculate every permutation of 2
                - ex) n = 2
                    2 main permutations:
                        1. 1 step, then 1 step
                        2. 2 step
                - ex) n = 3
                    1. (1, 1, 1)
                    2. (1, 2)
                    3. (2, 1)
            - Fibonacci sequence:
                - aggregate sum of possibilities of n - 1 and n, starting at 3
                    - sum = (n - 1) + (n - 2)
                    - ex) n = 5
                        at 0, 0 possibilities
                        at 1, 1 possibilities
                        at 2, 2 possibilities
                        at 3, (3 - 1) + (3 - 2) = 2 + 1 = 3 possibilities
                        at 4, (4 - 1) + (4 - 2) = 3 + 2 = 5 possibilities
                        at 5, (5 - 1) + (5 - 2) = 4 + 3 = 8 possibilities
        """
        if n < 3:
            return n

        first, second = 1, 2
        for i in range(3, n + 1):
            cur = first + second
            first, second = second, cur

        return second