class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        l_product = 1
        for i, num in enumerate(nums):
            res.append(l_product)
            l_product *= num

        r_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= r_product
            r_product *= nums[i]

        return res
        

        