from operator import add, sub, mul, truediv

class Solution:
    def __init__(self) -> None:
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_operands = ["+", "-", "/", "*"]
        operations = {
            "+": add,
            "-": sub,
            "/": truediv,
            "*": mul
        }

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if stack and token in valid_operands:
                left_operand, right_operand = int(stack[-2]), int(stack[-1])
                result = int(operations[token](left_operand,right_operand))
                
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(token)
        
        return stack[-1]