class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26

        for c in s1:
            s1_freq[ord(c) % 97] += 1

        for i, c in enumerate(s2):
            substring_freq = [0] * 26
            substring = s2[i:i + len(s1)]
            for l in substring:
                substring_freq[ord(l) % 97] += 1
            
            print(substring_freq)
            print(substring)
            if substring_freq == s1_freq:
                return True

        return False