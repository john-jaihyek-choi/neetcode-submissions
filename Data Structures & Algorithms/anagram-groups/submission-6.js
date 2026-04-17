class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    groupAnagrams(strs) {
        const res = {};
        
        for(const str of strs) {
            const charCount = new Array(26).fill(0);

            for (const char of str) {
                const charIndex = char.charCodeAt(0) - "a".charCodeAt(0);

                charCount[charIndex]++;
            }

            const uniqueCharCountKey = charCount.join(".");

            console.log(`logging uniqueCharCountKey ${uniqueCharCountKey}`);

            if(!res[uniqueCharCountKey]) {
                res[uniqueCharCountKey] = [];
            }
            
            res[uniqueCharCountKey].push(str);
        }

        return Object.values(res);
    }
}
