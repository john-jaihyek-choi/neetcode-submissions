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

        for i, c in enumerate(s1): # O(n)
            s1_count[ord(c) - ord('a')] += 1
            s2_substring_count[ord(s2[i]) - ord('a')] += 1
            
        if s1_count == s2_substring_count: # O(1)
            return True

        l = 0
        for r in range(s1_len, s2_len): # O(m - n)
            if s1_count == s2_substring_count: # O(26)
                return True
            
            r_index = ord(s2[r]) - ord('a')
            l_index = ord(s2[l]) - ord('a')
            s2_substring_count[r_index] += 1
            s2_substring_count[l_index] -= 1
            l += 1

        if s1_count == s2_substring_count:
            return True

        return False