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
            - TC: O(n) / SC: O(n)
        Two pointer solution:
            - high-level:
                - two pointer
                - check left and right
                    - if s[l] != s[r]:
                        - false
                    - else:
                        - true
                - if c not alnum, move pointer
        """
        # r = []
        # for c in s: # TC: O(n) / SC: O(1)
        #     if c.isalnum(): # TC: O(1) / SC: O(1)
        #        r.append(c.lower()) # TC: O(1) / SC: O(1)
        
        # new_s = "".join(r) # TC: O(n)
        # r = new_s[::-1]
        
        # return new_s == r

        l, r = 0, len(s)-1

        while len(s) > 1 and l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False    
            l += 1
            r -= 1

        return True
    