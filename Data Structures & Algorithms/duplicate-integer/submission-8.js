class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const new_nums = new Set()

        for(let i = 0; i < nums.length; i++){
            console.log(nums[i])
            if (new_nums.has(nums[i])) {
                return true
            } else {
                new_nums.add(nums[i])
            }
        }

        return false
    }

}
