class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_consecutive = 0

        for i in range(len(nums)):
            
            
            if (nums[i] - 1) not in nums_set: # checking for start of a sequence  
                consecutive = 1

                while nums[i] + consecutive in nums_set: # checking for continuous sequence while found
                    consecutive += 1
                
                longest_consecutive = max(consecutive, longest_consecutive)
        
        return longest_consecutive