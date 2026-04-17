class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Bruteforce:
            # sort the array O(n log n)
            # iterate and count the longest consecutive
        # Optimal solution:
            # initialize a set to store all unique values
            # iterate on the set (i = index, n = number)
                # consecutive = 1
                # while n - consecutive is in set:
                    # increment consecutive by 1
                # set the consecutive to max_consec vs consec
        
        num_set = set(nums)
        max_consec = 0
        for i, n in enumerate(nums):
            consecutive = 1
            while n - consecutive in num_set:
                consecutive += 1
            max_consec = max(max_consec, consecutive)

        return max_consec

                
        