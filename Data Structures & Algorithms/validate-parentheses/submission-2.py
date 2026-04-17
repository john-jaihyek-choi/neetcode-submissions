class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces_pair = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for c in s:
            if c == "{" or c == "(" or c == "[": # check for opening braces 
                stack.append(c)
            elif stack and stack[-1] == braces_pair[c]:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
