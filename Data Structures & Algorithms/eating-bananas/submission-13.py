class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Note:
            # The max number of bananas in pile represents the max amount of k it takes to finish within h
            # piles[i] = pile of bananas that could be eaten in a given hour
            # 

        # get max value of the piles (pile_max)
        # initialize a l and r pointer:
            # l = 1, r = pile_max
        # initialize a min_k = float('inf')
        # iterate the piles array while l <= r
            # ex)
                #     k
                # [1, 2, 3, 4]
            # set middle point, k, equal to (l + r) // 2 (k)
            # initialize an hour_to_finish = 0
            # iterate the piles array from 0
                # ex)
                    # k = 2
                    # [1, 4, 3, 2]
                # compute the hour to finish = math.ceil(piles[i] / k) and add to itself
            # if hour_to_finish < h:
                # set min_k equal to the minimum value of it itself or k
                # set l = k + 1
            # otherwise:
                # set r = k - 1
        # return min_k

        pile_max = max(piles)
        l, r = 1, pile_max
        min_k = pile_max

        while l <= r:
            k = (l + r) // 2
            hours_to_finish = 0

            for pile in piles:
                hours_to_finish += math.ceil(pile / k)

            if hours_to_finish > h:
                l = k + 1
            else:
                min_k = min(min_k, k)
                r = k - 1

        
        return min_k

