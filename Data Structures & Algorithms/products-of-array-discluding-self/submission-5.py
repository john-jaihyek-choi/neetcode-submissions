class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_arr = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res_arr[i] = res_arr[i-1] * nums[i-1]

        print(f"left_prod: {res_arr}")
        
        r_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res_arr[i] = res_arr[i] * r_product
            r_product *= nums[i]

        return res_arr