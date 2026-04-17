class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = float('inf')

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            mid = (r+l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                min_val = min(min_val, nums[mid])
                r = mid - 1
        
        return min_val