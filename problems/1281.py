class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        _sum = 0
        while n > 0:
            carry = n % 10
            product *= carry
            _sum += carry
            n //= 10

        return product - _sum