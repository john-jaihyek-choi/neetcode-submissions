class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        char_set = set()

        for r, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(c)
            res = max(res, r - l + 1)

        return res