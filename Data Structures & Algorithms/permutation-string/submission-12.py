from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)

        if s1_len > s2_len: # O(1)
            return False

        s1_count = [0] * 26
        s2_substring_count = [0] * 26
        matches = 0

        for i in range(len(s1)): # O(n)
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_substring_count[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            matches += 1 if s1_count[i] == s2_substring_count[i] else 0

        l = 0
        for r in range(s1_len, s2_len): # O(m - n)
            if matches == 26:
                return True
            # check for new right pointer index
            r_index = ord(s2[r]) - ord('a')
            s2_substring_count[r_index] += 1
            if s1_count[r_index] == s2_substring_count[r_index]:
                matches += 1
            elif s1_count[r_index] + 1 == s2_substring_count[r_index]:
                matches -= 1

            # check for new left pointer index
            l_index = ord(s2[l]) - ord('a')
            s2_substring_count[l_index] -= 1
            if s1_count[l_index] == s2_substring_count[l_index]:
                matches += 1
            elif s1_count[l_index] - 1 == s2_substring_count[l_index]:
                matches -= 1

            l += 1

        return matches == 26