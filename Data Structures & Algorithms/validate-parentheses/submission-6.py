class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_closing_parenthesis = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if stack and c in valid_closing_parenthesis:
                if valid_closing_parenthesis[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0 