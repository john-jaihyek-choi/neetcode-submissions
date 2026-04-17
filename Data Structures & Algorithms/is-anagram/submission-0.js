class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }

        const sLetters = {};
        const tLetters = {};
        
        for (let i = 0; i < s.length; i++) {
            sLetters[s[i]] = 1 + (sLetters[s[i]] || 0);
            tLetters[t[i]] = 1 + (tLetters[t[i]] || 0);
        }

        for (const letter in sLetters) {
            if(sLetters[letter] !== tLetters[letter]) return false;
        }

        return true;
    }
}
