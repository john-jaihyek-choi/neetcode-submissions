class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    // Input: nums = [4,5,6], target = 10
    // Output: [0,2]

    twoSum(nums, target) {
        const numsObj = {};

        for(let i = 0; i < nums.length; i++) {
            const complement = target - nums[i];

            if(complement in numsObj){
                return [numsObj[complement], i];
            }

            numsObj[nums[i]] = i;
            console.log(`logging numsObj = ${JSON.stringify(numsObj)}`)
        }
    }
}
