class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Note:
            # goal: return the length of the longest substring with one disttinct character after replacing up to k characters of the string
            # value to keep track of:
                # most frequent character count
                    # how: max value of new count value vs current max value
                # count map to store the letter counts

        # initialize a map to to store the letter counts (count_map)
        # initialize a frequent chracter count variable starting from 0 (max_freq)
        # initialize a variable to store the longest substing count starting from 0 (max_substring_count)
        # initialize left pointer starting from 0 (l)
        # iterate the s string from 0 (r = index, c = s[r])
            # increment count_map[c] by 1
            # set max_freq equal to max value between itself and count_map[c]
            # while length of the window (r - l - max_freq) IS NOT less than or equal to k:
                # increment l pointer by 1
            # set max_substring_count between r - l + 1 and itself
        # return max_substring_count

        count_map = defaultdict(int)
        max_freq, max_substring_count, l = 0, 0, 0

        for r, c in enumerate(s):
            count_map[c] += 1
            max_freq = max(max_freq, count_map[c])

            while not (r - l + 1 - max_freq) <= k:
                count_map[s[l]] -= 1
                l += 1
            
            max_substring_count = max(max_substring_count, r - l + 1)

        return max_substring_count
            