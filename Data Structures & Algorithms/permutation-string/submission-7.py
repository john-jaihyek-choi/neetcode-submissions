class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)

        if s1_len > s2_len:
            return False

        s1_count = dict()
        s2_substring_count = dict()

        for i in range(ord('a'), ord('z') + 1):
            s1_count[chr(i)] = 0
            s2_substring_count[chr(i)] = 0

        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_substring_count[s2[i]] += 1
            
        if s1_count == s2_substring_count:
            return True

        l = 0
        for r in range(s1_len, s2_len):
            if s1_count == s2_substring_count:
                return True

            s2_substring_count[s2[r]] += 1
            s2_substring_count[s2[l]] -= 1
            l += 1

        if s1_count == s2_substring_count:
            return True

        return False