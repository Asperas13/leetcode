class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        product = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product[i + j + 1] += int(num1[i]) * int(num2[j])
                product[i + j] += product[i + j + 1] // 10
                product[i + j + 1] %= 10

        i = 0
        while product[i] == 0:
            i += 1

        product = product[i:]
        return ''.join(list(map(str, product)))


