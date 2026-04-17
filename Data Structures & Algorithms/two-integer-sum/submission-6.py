class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Note:
            - find where nums[i] + nums[j] == target
            - i != j
            - exactly 1 pair of match
        Pseudocode:
            - Bruteforce (nested loop):
                - 2 nested loops, i starts 0, j starts i + 1
                    - if nums[i] + nums[j] == target:
                        - return True
                - return False
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]