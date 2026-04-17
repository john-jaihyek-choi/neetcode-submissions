class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_consec = 0

        for num in nums:
            consec = 1
            num_check = num - 1
            while num_check in nums_set:
                consec += 1
                num_check -= 1
            
            max_consec = max(max_consec, consec)

        return max_consec

            