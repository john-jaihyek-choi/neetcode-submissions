from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_arr = []
        repeat_map = defaultdict(set)
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if a in repeat_map['a']:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                if(
                    i == 1 and
                    l == 5 and
                    r == 9
                ):
                    print('bug')
                b = nums[l]
                c = nums[r]

                abc_sum = sum((a, nums[l], nums[r]))

                if abc_sum > 0:
                    r -= 1
                elif abc_sum < 0:
                    l += 1
                else:
                    res_arr.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    repeat_map['a'].add(a)
                    repeat_map['b'].add(nums[l])
                    repeat_map['c'].add(nums[r])

            print(f'{nums}')
        return res_arr