from string import digits

OPERATORS = '+-'
OPERANDS = set(digits)
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'

OPERATOR_TO_ACTION = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}


class Solution:
    def calculate(self, s: str) -> int:
        postfix = self.to_postfix(s)
        stack = []
        for token in postfix:
            if token in OPERATORS:
                right_operand = stack.pop()
                left_operand = stack.pop()
                result = OPERATOR_TO_ACTION[token](left_operand, right_operand)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]

    def to_postfix(self, expression):
        postfix = []
        stack = []
        i = 0
        while i < len(expression):
            if expression[i] in OPERANDS:
                digit = []
                while i < len(expression) and expression[i] in OPERANDS:
                    digit.append(expression[i])
                    i += 1
                stack.append(''.join(digit))
                continue
            elif expression[i] == OPEN_BRACKET:
                stack.append(OPEN_BRACKET)
            elif expression[i] == CLOSE_BRACKET:
                while stack and stack[-1] != OPEN_BRACKET:
                    postfix.append(stack.pop())
                stack.pop()
            elif expression[i] in OPERATORS:
                while stack and stack[-1] != OPEN_BRACKET:
                    postfix.append(stack.pop())
                stack.append(expression[i])
            i += 1

        while stack:
            postfix.append(stack.pop())
        return postfix


if __name__ == '__main__':
    s = Solution()
    print(s.calculate('(1+(4+5+2)-3)+(6+8)'))
    print(s.calculate(" 2-1 + 2 "))
    print(s.calculate('10 - 10 + 20 -20   + 30 - 30 + 40 - 41'))
