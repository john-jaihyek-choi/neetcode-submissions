class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_length_count = 0, 0
        repeat_map = set()

        for r, c in enumerate(s):
            while c in repeat_map:
                repeat_map.remove(s[l])
                l += 1
            max_length_count = max(max_length_count, r - l + 1)
            repeat_map.add(s[r])

        return max_length_count