class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_consecutive = 0
        for n in nums_set:
            consecutive = 1
            while n + consecutive in nums_set:
                consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)

        return max_consecutive