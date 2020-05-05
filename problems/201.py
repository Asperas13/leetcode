# 5 -> 101
# 6 -> 110
# 7 -> 111
# 8 -> 1000
# 6


def binary_number_size(n):
    s = -1
    while n:
        n >>= 1
        s += 1

    return s


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0
        while m and n:
            size_m = binary_number_size(m)
            size_n = binary_number_size(n)

            if size_m != size_n:
                return res

            leftmost_bit = 2 ** size_m
            res += leftmost_bit
            m -= leftmost_bit
            n -= leftmost_bit

        return res