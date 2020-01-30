from math import floor


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lo, hi = 2, x
        while lo <= hi:
            mid = (lo + hi) // 2

            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
            elif mid ** 2 > x:
                hi = mid - 1
            else:
                lo = mid + 1

        return hi

