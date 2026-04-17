class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        longest_substring_len = 0

        l = 0
        for r, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(c)
            longest_substring_len = max(longest_substring_len, r - l + 1)

        return longest_substring_len
            