class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parentheses = []

        def backtrace(opening, closing):
            if opening == closing == n:
                res.append(''.join(parentheses))
                return
            if opening < n: # check left
                parentheses.append('(')
                backtrace(opening + 1, closing)
                parentheses.pop()
            if closing < opening: # check right
                parentheses.append(')')
                backtrace(opening, closing + 1)
                parentheses.pop()
        
        backtrace(0, 0)

        return res