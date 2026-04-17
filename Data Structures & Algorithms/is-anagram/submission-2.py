class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_count = dict()
        t_letter_count = dict()

        for c in s:
            s_letter_count[c] = s_letter_count.get(c, 0) + 1

        for c in t:
            t_letter_count[c] = t_letter_count.get(c, 0) + 1
        
        return s_letter_count == t_letter_count
