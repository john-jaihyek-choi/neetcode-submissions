class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_length = 0, 0
        repeat_map = set()

        for i, c in enumerate(s):
            while c in repeat_map:
                repeat_map.remove(s[l])
                l += 1
            repeat_map.add(c)
            max_length = max(max_length, i - l + 1)
        
        return max_length