class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))

        if len(s1) > len(s2):
            return False

        for i in range(0, len(s2)):
            sorted_substring = "".join(sorted(s2[i:(i + len(s1))]))
            if sorted_substring == sorted_s1:
                return True

        return False