class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input:
            # s: str
                # s only consists of ASCII characters
        # output:
            # output: int
                # length of the longest substring without duplicates
        # goal:
            # given string s, return the length of the longest substring without duplicate characters
        # Braintstorm:
            # Bruteforce:
                # iterate on s where i = index
                    # iterate beginning s[i + 1] where j is second index until s[j] == currently existing char
                        # if existing char found
                            # break the loop
                        # otherwise
                            # set the max_substring_length to j - i + 1
        # Potential Edge-cases:
            # empty string s?
                # the constraint of the problem shows there won't be an empty string
            # single string?
                # return 1
        # Variables:
            # max_substring_length: int
            # letter_set: set
                # stores the chracters at each index in s such that I can access the char constant time

        # Bruteforce (TC: O(n^2) / SC: O(n))
        # Pseudocode:
            # initialize the max_substring_length
                # max_substring_length = 0
            # iterate on the s string
                # where:
                    # i = index
                    # c = s[i]
                # initialize an set with a 
                    # letter_set = set(c)
                # iterate on the s string
                    # where:
                        # beginning at s[i + 1]
                        # j = index
                    # check if s[j] in letter_set:
                        # set the max_substring:
                            # max_substring_length = max(max_substring_length, j - i)
                        # break out of the loop
                    # otherwise:
                        # add the s[j] to the letter_set
                # remove c from the letter_set:
                    # letter_set.remove(c)
        
        # max_substring_length = 0

        # for i, c in enumerate(s): # O(n)
        #     letter_set = set()
        #     for j in range(i, len(s)): # O(n)
        #         if s[j] in letter_set:
        #             max_substring_length = max(max_substring_length, j - i)
        #             break
        #         letter_set.add(s[j])

        # return max_substring_length                
        
        # Optimal Solution (TC: / SC:)
        # sliding window approach:
            # use two pointers to create a window
                # expand the window (move r pointer):
                    # as long as s[r] is not in the letter_set
                # reduce the window (move l pointer):
                    # until s[r] is no longer in the letter_set
                    # remove s[l] from the letter set before shifting 
        # Variables:
            # max_substring_length: int
            # letter_set: set
            # l: int
                # beginning at 0
        # Pseudocode:
            # initialize a max_substring_length:
                # max_substring_length = 0
            # letter_set = set()
            # initialize l pointer for window:
                # l = 0
            # iterate on s (r = index, c = s[r])
                # while c in letter_set:
                    # set the max_substring_length:
                        # max_substring_length = max(max_substring_length, r - l)
                    # remove s[l] from letter_set:
                        # letter_set.remove(s[l])
                    # increment l by 1:
                        # l += 1
                # otherwise:
                    # add c to letter_set:
                        # letter_set.add(c)
        max_substring_length = 0
        letter_set = set()
        l = 0
        for r, c in enumerate(s):
            while c in letter_set:
                letter_set.remove(s[l])
                l += 1
            letter_set.add(c)
            
            max_substring_length = max(max_substring_length, r - l + 1)
        
        return max_substring_length




            