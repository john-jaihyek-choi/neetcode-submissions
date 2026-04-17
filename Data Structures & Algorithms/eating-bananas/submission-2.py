class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            k = (r + l) // 2
            
            hrs_to_finish = 0
            for pile in piles:
                hrs_to_finish += math.ceil(pile / k)

            if hrs_to_finish > h:
                l = k + 1
            else:
                min_k = min(min_k, k)
                r = k - 1
                

        return min_k