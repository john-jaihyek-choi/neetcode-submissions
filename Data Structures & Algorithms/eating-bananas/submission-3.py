class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        #  l  m     r
        # [1, 2, 3, 4]

        k = max_k

             
        l, r = 1, max_k
        while l <= r:
            m = (l + r) // 2

            hrs_to_finish = 0
            for banana_to_eat in piles:
                hrs_to_finish += math.ceil(banana_to_eat / m)

            if hrs_to_finish <= h:
                k = m
                r = m - 1
            else:
                l = m + 1

        return k