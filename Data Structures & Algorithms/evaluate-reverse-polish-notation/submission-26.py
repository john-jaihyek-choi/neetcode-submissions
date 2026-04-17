from operator import add, sub, mul, truediv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Note:
            # When using RPN for - and /, the order of the number is crucial
            # stack can be used to maintain the order
                # stack[-1] = immediately previous value
                # stack[-2] = second from the previous value
            
        # stack = []
        # operator_sets = set({"+", "-", "*", "/"})

        # for token in tokens:
        #     if stack and token in operator_sets:
        #         b, a = int(stack.pop()), int(stack.pop())

        #         if token == "+":
        #             stack.append(a + b)
        #         elif token == "*":
        #             stack.append(a * b)
        #         elif token == "-":
        #             stack.append(a - b)
        #         elif token == "/":
        #             stack.append(a / b)

        #         continue

        #     stack.append(token)

        # return int(stack[-1])

        # using dynamic operator
        stack = []
        operator_sets = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv,
        }

        for token in tokens:
            if stack and token in operator_sets:
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(operator_sets[token](a, b))
                continue

            stack.append(token)

        return int(stack[-1])
