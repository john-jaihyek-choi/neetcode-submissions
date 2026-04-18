class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Note:
            - returned output can be in any order
            - i != j != k
        Bruteforce:
            - 3 loops
                - i, j, k
                - if n[i] + n[j] + n[k] == 0
                    - append triplet to output
                - TC: O(n^3) / SC: O(n) or O(1) without res_arr
        Sort + Two Pointer:
            - sort nums
            - iterate on nums
                - initialize two pointer
                    - l, r = i+1, len(nums)
                - while l < r:
                    - if n[i] + n[l] + n[r] > 0:
                        - r-=1
                    - if n[i] + n[l] + n[r] < 0:
                        - l+=1
                    - else:
                        res.append([n[i],n[j],n[l]])
            - Example
                [-4, -1, -1, 0, 1, 2]
        """

        res = []
        nums.sort()
        for i in range(len(nums)-1):
            l, r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return res

        