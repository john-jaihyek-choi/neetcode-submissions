class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # input:
            # s = string
                # UPPERCASE english characters
            # k = int
                # represents the maximum number of replacements allowed
        # goal: return length of the longest substring which contains only one distinct character
        # sliding window approach:
            # l and r pointer
                # when does l move?
                    # when replacements (k) are all used up
                # when does r move?
                    # as long as replacements are within k
            # How to know how many replacements to make?
                # if we know the count of the most frequently appearing letter, we can to window - most frequent count
            # How can I keep track of most frequently appearing char count?
                # use a dictionary and store the char as a key and set the count
                # in each iteration, update the max_freq count
            # Do I need to decrease the max_freq count when moving l?
                # no, the goal is to find the the max repeating substring
                    # so there's no need for us to make the window smaller
                        # this means when l moves, r won't stop and move with it
        # variables needed:
            # max_freq: int
            # l: int
            # r: int
            # char_count: dict

        # Pseudocode:
            # initialize an empty dictionary for char count (char_count)
                # use defaultdict with int as a default value
            # initialize max freq to 0 (max_freq)
            # initialize l pointer:
                # l to start at 0
            # loop the s string (r = index, c = s[r])
                # increment c's count in char_count
                # set max_freq to bigger value of itself or char_count[c]
                # if the size of the window (r - l + 1) minus the max_freq is bigger than k:
                    # decrement the s[l] count in char_count
                    # increment l pointer
            # return r - l + 1

        char_count = defaultdict(int)
        max_freq, l = 0, 0
        for r, c in enumerate(s):
            char_count[c] += 1
            max_freq = max(max_freq, char_count[c])

            if (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1

        return r - l + 1

        