class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        l = 0
        max_length = 0
        for r, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(c)
            max_length = max(max_length, r - l + 1)
        return max_length