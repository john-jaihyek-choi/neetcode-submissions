class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Intuition:
            Bruteforce:
                - sort the stones
                - while len(stones) > 1:
                    - pop the last 2 elements as long as num is non-empty
                        - x = stones.pop()
                        - y = stones.pop()
                    - if x == y:
                        continue to next iteration
                    - elif x < y:
                        y = y - x
                        stones.append(y)
                        sort stones
                    - else:
                        x = x - y
                        stones.append(x)
                        sort stones
                - return stones[0]
        """
        # TC: O(n * n log n) / SC: O(1)
        stones.sort() # TC: O(n log n)
        while len(stones) > 1: # TC: O(n - 1) -> O(n)
            x, y = stones.pop(), stones.pop() 

            if x == y:
                continue
            elif x < y:
                stones.append(y - x)
            else:
                stones.append(x - y)

            stones.sort() # TC: O(n log n)
        return stones[0] if stones else 0