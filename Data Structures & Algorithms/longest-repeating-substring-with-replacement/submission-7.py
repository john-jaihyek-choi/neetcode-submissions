class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = dict()
        max_length, l = 0, 0

        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            
            most_freq_c_count = 0
            for count in char_count.values():
                most_freq_c_count = max(most_freq_c_count, count)

            if (len(s[l:r+1])) - most_freq_c_count > k:
                char_count[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length