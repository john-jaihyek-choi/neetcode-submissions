class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        // const productArr = [];

        // let prefixProduct = 1;
        // for(let i = 0; i < nums.length; i++) {
        //     productArr[i] = prefixProduct; 
        //     prefixProduct *= nums[i];
        // }

        // console.log(productArr);

        // let postfixProduct = 1;
        // for(let i = productArr.length - 2; i >= 0; i--) {
        //     postfixProduct *= nums[i + 1];
        //     productArr[i] *= postfixProduct;
        // }

        // return productArr;

        const responseArr = [];
        
        for (let i = 0; i < nums.length; i++) {
            let product = 1;

            for (let j = 0; j < nums.length; j++) {
                if(i !== j) {
                    product *= nums[j];
                }
            }

            responseArr.push(product);
        }

        return responseArr;
    }
}
