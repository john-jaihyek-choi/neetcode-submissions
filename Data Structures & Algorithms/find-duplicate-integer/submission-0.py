class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Obvious solution: store the num in a set, then detect duplicate
            # initialize an empty set (or set(nums) since nums is guaranteed to be List[int]) (num_set)
            # set cur to head to iterate on
            # while cur is valid:
                # if cur.val is in num_set:
                    # return cur.val
                # num_set.add(cur.val)
            # return 0

        nums_set = set()
        for n in nums:
            if n in nums_set:
                return n
            nums_set.add(n)
        return 0