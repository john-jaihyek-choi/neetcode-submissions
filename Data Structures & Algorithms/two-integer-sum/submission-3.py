class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_map = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in compliment_map:
                return [compliment_map[compliment], i]
            
            compliment_map[num] = i