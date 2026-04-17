from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)

        if s1_len > s2_len: # O(1)
            return False

        s1_count = dict()
        s2_substring_count = dict()
        matches = 0

        for i in range(ord('a'), ord('z') + 1): # O(26)
            s1_count[chr(i)] = 0
            s2_substring_count[chr(i)] = 0

        for i in range(len(s1)): # O(n)
            s1_count[s1[i]] += 1
            s2_substring_count[s2[i]] += 1

        for c in s1_count.keys():
            if s1_count[c] == s2_substring_count[c]:
                matches += 1

        #  s1 = 'ab' s2 = 'lecabee'
        l = 0
        for r in range(s1_len, s2_len): # O(m - n)
            if matches == 26:
                return True
            # check for new right pointer index
            s2_substring_count[s2[r]] += 1
            if s1_count[s2[r]] == s2_substring_count[s2[r]]:
                matches += 1
            elif s1_count[s2[r]] + 1 == s2_substring_count[s2[r]]:
                matches -= 1

            # check for new left pointer index
            s2_substring_count[s2[l]] -= 1
            if s1_count[s2[l]] == s2_substring_count[s2[l]]:
                matches += 1
            elif s1_count[s2[l]] - 1 == s2_substring_count[s2[l]]:
                matches -= 1

            l += 1

        return matches == 26