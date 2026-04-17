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
                        at f(0), 0 possibilities
                        at f(1), 1 possibilities
                        at f(2), 2 possibilities
                        at f(3), f(3 - 1) + f(3 - 2) = f(2) + f(1) = 1 + 2 = 3 possibilities
                        at f(4), f(4 - 1) + f(4 - 2) = f(3) + (2) = 3 + 2 = 5 possibilities
                        at f(5), f(5 - 1) + f(5 - 2) = f(4) + f(3) = 5 + 3 possibilities
        """
        # if n < 3:
        #     return n

        # first, second = 1, 2
        # for i in range(3, n + 1):
        #     cur = first + second
        #     first, second = second, cur

        # return second

        # dynamic programming:
        if n <= 2:
            return n

        array = [0] * (n + 1)
        array[1], array[2] = 1, 2

        for i in range(3, n + 1):
            array[i] = array[i - 1] + array[i - 2]

        return array[n]





