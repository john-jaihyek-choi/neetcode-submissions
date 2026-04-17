class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    // Input: nums = [4,5,6], target = 10
    // Output: [0,2]

    twoSum(nums, target) {
        // Solution 1:
        // const numsObj = {};

        // for(let i = 0; i < nums.length; i++) {
        //     const complement = target - nums[i];

        //     if(complement in numsObj){
        //         return [numsObj[complement], i];
        //     }

        //     numsObj[nums[i]] = i;
        //     console.log(`logging numsObj = ${JSON.stringify(numsObj)}`)
        // }

        // Solution 2:
        const numsMap = new Map();

        for(let i = 0; i < nums.length; i++) {
            const currentNum = nums[i];
            const complement = target - currentNum;
            const sumIndex = numsMap.get(complement);

            const isTarget = numsMap.has(complement);
            if(isTarget){
                return i < sumIndex ? [i, sumIndex] : [sumIndex, i];
            }

            numsMap.set(currentNum, i);
        }
    }
}
