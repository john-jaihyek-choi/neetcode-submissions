class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = string
        # goal: find substring WITHOUT duplicate characters
        # Brainstorm:
            # how to go about keeping count of the char
                # use set
            # two pointers - left and right
                # when does left move?
                    # moves when encounters s[i] that's already in the set
                # when does right move?
                    # moves as long as it doesn't encounter s[i] that's in the set
            # Does the window have to contract?
                # Yes, the window must contract until s[l] finds the duplicate letter
                    # what does this mean?
                        # WHILE s[r] exists in char_set, l moves and removes the letters in char_set
                    # anything to look out for?
                        # the s[l] items still need to be removed as l moves
            # What's being returned?
                # the length of the longest substring
                # do I need to initialize and keep it updated?
                    # yes, I'll have to keep updated for edge cases such as repeating duplicate characters
        # Pseudocode:
            # initialize a set to store the characters iterating (char_set)
            # initialize l pointer:
                # l starting from 0 (l)
            # loop len(s) - 1 many times (r = index)
                # set char for easy access:
                # while char in char_set:
                    # remove s[l] from the char_set
                    # l += 1
                # add the s[r] to char_set
            # return r - l + 1

        char_set = set()
        l = 0
        max_substring = 0
        for r, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(c)
            max_substring = max(max_substring, r - l + 1)
        
        return max_substring

            