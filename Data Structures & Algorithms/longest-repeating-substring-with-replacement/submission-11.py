class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_count = dict()
        max_c_count = 0

        l = 0
        for r, c in enumerate(s):
            c_count[c] = c_count.get(c, 0) + 1
            max_c_count = max(max_c_count, c_count[c])

            if (r - l + 1) - max_c_count > k:
                c_count[s[l]] -= 1
                l += 1

        return r - l + 1

            
