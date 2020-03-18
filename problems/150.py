class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def _add(x, y):
            return x + y

        def _substract(x, y):
            return x - y

        def _multiply(x, y):
            return x * y

        def _divide(x, y):
            return int(x / y)

        OPERATORS = {'+': _add, '-': _substract, '*': _multiply, '/': _divide}
        for token in tokens:
            if OPERATORS.get(token):
                operator = OPERATORS.get(token)
                operand_y, operand_x = int(stack.pop()), int(stack.pop())
                stack.append(operator(operand_x, operand_y))
            else:
                stack.append(token)

        return stack.pop()