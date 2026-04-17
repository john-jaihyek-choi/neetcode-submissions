class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r = 0, k

        while r <= len(nums):
            output.append(max(nums[l:r]))
            l += 1
            r += 1

        return output
