class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        count_map = defaultdict(int)

        for r, c in enumerate(s):
            count_map[c] += 1
            max_freq = max(max_freq, count_map[c])

            if r - l + 1 - max_freq > k:
                count_map[s[l]] -= 1
                l += 1
            
        return r - l + 1