class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # input:
            # s: str
            # t: str
        # goal: find the shortest substring of s in t
            # includes dupliates
            # if no substring, return empty string
            # always unique output
        # Note:
            # since we need to find substring of s that includes all letters in t
                # len(s) cannot be less than t
                    # if len(s) < t, return ""
            # only uppercase and lowercase english characters
        # Sliding window approach:
            # l and r pointers
                # when does r move?
                    # as long as we r - l doesn't have every letter in t
                # when does l move?
                    # once r - l has every letter in t
            # How to know if window contains the letters?
                # we can keep track of the counts of characters in t
                    # no need to keep count of characters outside of t
                # array hashing vs dictionary:
                    # array hashing:
                        # we'll need to consider 2 casing
                            # we can change the lower to upper or vice versa
                    # dictionary:
                        # no need for casing concerns
                        # defaultdict for easy int counting
                        # O(1) access
            # iterate together or separate?
                # separate:
                    # iterate t initially for the count of each characters
                        # once t's characters are counted, we know the total number of UNIQUE characters needed
                    # first (len(t)) part of the s char could also be tracked along with t
                        # we can use this to immediately return the substring if they are exact match
                            # we are finding min substring, so if s's t_len portion matches, it's a match
                    # iterate the remainder of s starting from where we left off
            # Knowing the need count, how can we count the "have"?
                # As long as the s[r] count in s_count is == count in t_count:
                    # we can increment have
                        # if greater, we still qualify, so we won't count
            # Does the window need to contract?
                # yes, the window should get smaller while have == need
            # Return value?
                # should return a substring
                    # do we need to keep track of the substring?
                        # yes, since window size will change dynamically throughout the iteration
        # Variables to track:
            # t_count: dict
            # s_count: dict
            # need: int
            # have: int
            # min_len: int
                # we can use float("-inf") as an initial value
            # substring_pair: List[int] -> [l, r + 1]

        # Pseudocode:
            # initialize min_len to float("-inf")
            # initialize substring_pair to [-1, -1]
            # initialize t_count and s_count dictionaries
                # use defaultdict int for easy increment
            # iterate the t string (i = index, c = t[i])
                # store the count of each string to t_count
            # set need to len(t_count)
            # set have to 0
            # initialize l pointer:
                # l = 0
            # iterate the s string (r = index, c = s[i])
                # if c in s_count
                    # increment s_count[c] by 1
                # if s_count[c] == t_count[c]:
                    # increment the "have" by 1
                # while have == need:
                    # if min_len > window size (r - l + 1):
                        # set min_len to smaller of itself or r - l + 1
                        # substring_pair = [l, r + 1]
                    # if s[l] in t_count:
                        # decrement s[l] in s_count by 1
                    # if s_count[s[l]] < t_count[s[l]]:
                        # decrement have by 1
                    # increment l by 1
            # l, r = substring_pair
            # return s[l, r]

        min_len = float('inf')
        substring_pair = [-1, -1]
        t_count, s_count = defaultdict(int), defaultdict(int)
        
        for c in t:
            t_count[c] += 1

        have, need = 0, len(t_count)
        l = 0
        for r, c in enumerate(s):
            s_count[c] += 1
            
            if c in t_count and s_count[c] == t_count[c]:
                have += 1

            while have == need:
                if min_len > (r - l + 1):
                    min_len = min(min_len, r - l + 1)
                    substring_pair = [l, r + 1]

                s_count[s[l]] -= 1

                if s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        l, r = substring_pair


        return s[l:r]



        
        
            