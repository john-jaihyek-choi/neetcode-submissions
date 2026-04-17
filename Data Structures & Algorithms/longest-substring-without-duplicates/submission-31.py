class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        valid_substring = set()

        l = 0
        max_length = 0
        for r, c in enumerate(s):
            while c in valid_substring:
                valid_substring.remove(s[l])
                l+=1
            valid_substring.add(c)
            max_length = max(max_length, r - l + 1)
        return max_length