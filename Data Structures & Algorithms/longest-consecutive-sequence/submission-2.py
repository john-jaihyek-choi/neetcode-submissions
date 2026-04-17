class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_consecutive = 0

        for n in nums:
            if n - 1 not in nums_set:
                consecutive = 1
                
                while n + consecutive in nums_set:
                    consecutive += 1
                
                max_consecutive = max(consecutive, max_consecutive)
        return max_consecutive
            

