class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    // hasDuplicate(nums) {
    //     if(!nums || nums.length === 0) {
    //         return false;
    //     };

    //     const numObj = {};

    //     for(let i = 0; i < nums.length; i++){
    //         if(numObj[nums[i]]) {
    //             return true;
    //         } else {
    //             numObj[nums[i]] = true;
    //         }
    //     }

    //     return false;
    // }
    hasDuplicate(nums) {
        const numsSet = new Set();
        for (const num of nums) {
            if(numsSet.has(num)) return true;

            numsSet.add(num);
        }

        return false;
    }
}
