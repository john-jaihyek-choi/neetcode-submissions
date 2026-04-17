class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Note:
            - if palindrome -> true
                - else -> false
            - case insensitive
            - ignore non numeric characters
        First thought solution:
            - remove spaces/non-alphanumerics
            - reverse s compare with original
        Two pointer solution:
            - high-level:
                - two pointer
                - remove empty spaces
                - check left and right
                    - if s[l] != s[r]:
                        - false
                    - else:
                        - true
        """
        r = []
        for c in s:
            if c.isalnum():
               r.append(c.lower())
        
        new_s = "".join(r)
        r = new_s[::-1]
        
        return new_s == r
    