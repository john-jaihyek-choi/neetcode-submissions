class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0

        for r in range(k, len(nums) + 1): # O(n)
            output.append(max(nums[l:r])) # O(n)
            l+=1

        return output
