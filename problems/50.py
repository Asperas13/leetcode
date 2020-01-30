class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        cur_pow = 1
        x = (1 / x) if n < 0 else x
        base = x
        if n < 0:
            n = -n
        powers = 0
        while cur_pow < n:
            if cur_pow * 2 <= n:
                x = x ** 2
                cur_pow *= 2
            else:
                powers = powers * x if powers else x
                x = base
                n -= cur_pow
                cur_pow = 1

        powers = powers * x if powers else x
        return powers