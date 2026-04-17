from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_arr = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                abc_sum = sum((a, nums[l], nums[r]))

                if abc_sum > 0:
                    r -= 1
                elif abc_sum < 0:
                    l += 1
                else:
                    res_arr.append([a, nums[l], nums[r]])
                    l += 1
                    # r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res_arr