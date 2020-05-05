from math import factorial
# permutation(n) + permutation(n) * permutation(n)

class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        return (factorial(2*n) // (2**n)) % (10**9 + 7)