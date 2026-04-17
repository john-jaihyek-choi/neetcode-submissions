class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces_pair = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for c in s: # O(n)
            if c not in braces_pair: # check for opening braces 
                stack.append(c)
            elif stack and stack[-1] == braces_pair[c]: # check for closing braces pair
                stack.pop()
            else: # if neither, return false
                return False
            
        return len(stack) == 0
