class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length_count = 0
        repeat_map = set()

        while r < len(s):
            while s[r] in repeat_map:
                repeat_map.remove(s[l])
                l += 1
            max_length_count = max(max_length_count, r - l + 1)
            repeat_map.add(s[r])
            r += 1
            
        return max_length_count