from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first:
            # sort the nums array
                # use the builtin sort() method on nums
                # OR
                # use the sorted() method

        # second:
            # single iterator to check the first number
                # initialize an empty array to store the res output = res
                # iterate the nums array from 0 (i = index)
                # initialize the l and r pointer
                    # l = i + 1
                    # r = len(nums) - 1
        
        # third:
            # two-pointer, 2 number sum, to check the remaining two combination
                # while l < r:
                    # if nums[l] + nums[r] < target:
                        # l += 1
                    # elif nums[l] + nums[r] > target:
                        # r -= 1
                    # else:
                        # return res.append([nums[i], nums[l], nums[r]])
        # return the res

        nums.sort()
        res = []
        # triplet_set = set()

        for i, n in enumerate(nums): # O(n)
            if i > 0 and n == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        # res = []
        # for triplet in triplet_set:
        #     i, j, k = triplet
        #     res.append([i, j, k])

        return res