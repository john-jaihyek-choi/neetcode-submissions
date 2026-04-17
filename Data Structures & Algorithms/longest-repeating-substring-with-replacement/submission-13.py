class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = defaultdict(int)
        max_occurance = 0
        longest_substring = 0
        l = 0
        for r, c in enumerate(s):
            count_dict[c] += 1
            max_occurance = max(max_occurance, count_dict[c])

            while r - l + 1 - max_occurance > k:
                count_dict[s[l]] -= 1
                l += 1

        return r - l + 1

            
