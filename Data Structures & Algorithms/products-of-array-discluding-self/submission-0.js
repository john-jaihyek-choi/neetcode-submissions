class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const productArr = [];

        let prefixProduct = 1;
        for(let i = 0; i < nums.length; i++) {
            productArr[i] = prefixProduct; 
            prefixProduct *= nums[i];
        }

        console.log(productArr);

        let postfixProduct = 1;
        for(let i = productArr.length - 2; i >= 0; i--) {
            postfixProduct *= nums[i + 1];
            productArr[i] *= postfixProduct;
        }

        return productArr;
    }
}
