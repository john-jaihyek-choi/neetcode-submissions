class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Note:
            # ex) [3, 4, 5, 6, 1, 2]
            # if l < m < r:
                # array is fully sorted
            # if l < m > r:
                # right half of the array is part of the rotated array
            # if l > m < r:
                # left half of the array is part of the rotated array
            # Goal: find the INDEX of the target within nums
                # Possible conditions
                    # When m == target:
                        # target found
                    # When l < m: (Left sorted):
                        # if target < m:
                            # r = m - 1
                        # else:
                            # l = m + 1
                    # When m < r: (Right sorted)
                        # if m < target:
                            # l = m + 1
                        # else:
                            # r = m - 1

        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            left, mid, right = nums[l], nums[m], nums[r]

            if mid == target:
                return m
            elif left <= mid: # Left-side sorted
                if left <= target < mid:
                    r = m - 1
                else:
                    l = m + 1
            else: # Right-side sorted
                if mid < target <= right:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1


                






