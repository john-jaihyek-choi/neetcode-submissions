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
                right_operand = stack.pop()
                left_operand = stack.pop()

                result = int(operations[token](left_operand, right_operand))
                
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[-1]