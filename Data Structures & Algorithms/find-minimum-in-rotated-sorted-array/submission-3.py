class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ex) 
            #   l     m        r
            # [ 3, 4, 5, 6, 1, 2 ]
        # Note:
            # if m < r
                # right half is sorted
            # if l < m
                # left half is sorted
            # if l < m < r
                # nums is sorted
            # if m > r
                # right half is the rotated part of the array
            # if m < l
                # left half is the rotated part of the array
        
        # initialize l and r pointer
        # initialize a min_val = float('inf')
        # while l <= r
            # calculate m, (l + r) // 2
            # set min_val equal to min of itself vs m
            # if m > r:
                # set l = m + 1
            # else:
                # set r = m - 1
        # return min_val

        l, r = 0, len(nums) - 1
        min_val = float('inf')
        while l <= r:
            m = (l + r) // 2
            min_val = min(min_val, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return min_val