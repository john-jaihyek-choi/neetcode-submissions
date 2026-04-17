class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        if(!nums || nums.length === 0) {
            return false;
        };

        const numObj = {};

        for(let i = 0; i < nums.length; i++){
            console.log(`checking if ${nums[i]} exists`);
            if(numObj[nums[i]]) {
                return true;
            } else {
                numObj[nums[i]] = true;
            }
        }

        return false;
    }
}
