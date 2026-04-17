class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    // nums = [1,2,2,3,3,3], k = 2;
    topKFrequent(nums, k) {
        const countObj = {};
        for(let num of nums) {
            if (!countObj[num]) {
                countObj[num] = 0;
            } 

            countObj[num]++;
        }

        const countArr = Array.from({ length: nums.length + 1 }, () => []);

        for (const num in countObj) {
            const number = num;
            const count = countObj[num];
            countArr[count].push(parseInt(number));
        }

        console.log(countArr);

        const responseArr = [];

        for (let i = countArr.length - 1; i > 0; i--) {
            for(const number of countArr[i]) {
                responseArr.push(number);

                if(responseArr.length >= k) {
                    return responseArr;
                }
            }
        }

        return responseArr;
    }
}
