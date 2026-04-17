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
                    - else:
                        x = x - y
                        stones.append(x)
                - return stones[0]
        """
        stones.sort()
        while len(stones) > 1:
            x, y = stones.pop(), stones.pop()
            
            if x == y:
                continue
            elif x < y:
                stones.append(y - x)
                stones.sort()
            else:
                stones.append(x - y)
                stones.sort()

        print(stones)
        
        return stones[0] if stones else 0