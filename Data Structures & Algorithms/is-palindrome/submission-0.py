class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = ''

        for c in s:
            lower_c = c.lower()
            if lower_c.isalnum():
                formatted_s += lower_c

        l = 0
        r = len(formatted_s) - 1

        while l < r:
            if formatted_s[l] != formatted_s[r]:
                return False
            l += 1
            r -= 1

        return True