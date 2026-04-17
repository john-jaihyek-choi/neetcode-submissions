class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_length = len(nums)
        res_arr = []
        l_product = 1

        for i in range(num_length):
            l_product *= 1 if i <= 0 else nums[i-1]
            res_arr.append(l_product)

        # right_products = []
        r_product = 1
        for i in range(num_length-1, -1, -1):
            r_product *= 1 if i >= num_length - 1 else nums[i+1]
            res_arr[i] *= r_product

        return res_arr