class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Note:
            # sliding window approach
            # use set to keep a set of characters
            # l and r start from 0
            # if s[r] in set, increment l by 1
            
        letter_set, l = set(), 0
        max_substring = 0
        for r, c in enumerate(s):

            while c in letter_set:
                letter_set.remove(s[l])
                l += 1
                
            letter_set.add(c)
            max_substring = max(max_substring, r - l + 1)

        return max_substring