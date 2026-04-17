class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # check if alpha numeric
            # check if lower vs upper
            while l < r and not self.is_alphanumeric(s[l]):
                l += 1
            while l < r and not self.is_alphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        return True

    def is_alphanumeric(self, c: str) -> bool:
        if (
            ord('A') <= ord(c) <= ord('Z')
            or ord('a') <= ord(c) <= ord('z')
            or ord('0') <= ord(c) <= ord('9')
        ):
            return True

        return False