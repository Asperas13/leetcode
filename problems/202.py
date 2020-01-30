class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        def _calculate_new_number(num):
            sum_of_squares = 0

            while num > 0:
                sum_of_squares += (num % 10) ** 2
                num = num // 10

            return sum_of_squares

        while True:
            if n == 1:
                return True

            if n in seen:
                return False

            seen[n] = True

            n = _calculate_new_number(n)

        return False

