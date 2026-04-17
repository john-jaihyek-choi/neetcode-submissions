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

        sorted_nums = sorted(nums)
        triplet_set = set()

        for i in range(len(sorted_nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if sorted_nums[i] + sorted_nums[l] + sorted_nums[r] < 0:
                    l += 1
                elif sorted_nums[i] + sorted_nums[l] + sorted_nums[r] > 0:
                    r -= 1
                else:
                    triplet_set.add(tuple([sorted_nums[i], sorted_nums[l], sorted_nums[r]]))
                    l += 1

        res = []
        for triplet in triplet_set:
            i, j, k = triplet
            res.append([i, j, k])

        return res