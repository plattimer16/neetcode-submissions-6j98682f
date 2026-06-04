class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(op1: int, op2: int) -> int:
            return op1 + op2
        def sub(op1: int, op2: int) -> int:
            return op1 - op2
        def multiply(op1: int, op2: int) -> int:
            return op1*op2
        def divide(op1: int, op2: int) -> int:
            return op1/op2
        operators = {'+': add, '-': sub, '/': divide, '*': multiply}
        stack = []
        for x in tokens:
            if x in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                res = operators[x](int(op1), int(op2))
                stack.append(res)
            else:
                stack.append(x)

            print(stack)
        return int(stack.pop())
