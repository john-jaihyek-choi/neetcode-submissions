class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_parenthesis = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for c in s:
            if c in closing_parenthesis:
                if stack and closing_parenthesis[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0