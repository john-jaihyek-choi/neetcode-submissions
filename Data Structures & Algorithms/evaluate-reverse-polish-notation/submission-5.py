class Solution:
    def __init__(self) -> None:
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if stack and self.isValidOperand(token):
                num, temp = int(stack[-2]), int(stack[-1])

                if token == "+":
                    num += temp
                elif token == "-":
                    num -= temp
                elif token == "*":
                    num *= temp
                elif token == "/":
                    num /= temp

                stack.pop()
                stack.pop()
                stack.append(int(num))
            else:
                stack.append(token)
        
        return stack[-1]
    
    def isValidOperand(self, operand: str):
        operand_list = ["+", "-", "/", "*"]

        return operand in operand_list