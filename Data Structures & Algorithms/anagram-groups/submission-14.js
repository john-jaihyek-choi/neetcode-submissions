class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    // bruteforce solution: sort each words, set each sorted word as hash key
    groupAnagrams(strs) {
        // steps:
            // defined hashmap
            // iterate on strs
                // sort the word
                // take the worted word register to hashmap
                    // if already exists:
                        // append str to the existing value
                    // else:
                        // create a new array with str as the 0th value
            // iterate on the hashmap
                // append all values in hashmap to res (Array)
        const hashmap = {}
        for (const word of strs) {
            const sorted_word = word.split("").sort().join("")
            if (sorted_word in hashmap) {
                hashmap[sorted_word].push(word)
            } else {
                hashmap[sorted_word] = [word]
            }
        }
        
        const res = []
        for (const words of Object.values(hashmap)) {
            res.push(words)
        }

        return res

    }
}
