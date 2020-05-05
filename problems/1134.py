class Solution:
    def isArmstrong(self, N: int) -> bool:
        digits = []

        k = N
        while k > 0:
            digits.append(k % 10)
            k //= 10

        lo, hi = 0, 32

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            total = 0
            for digit in digits:
                total += digit ** mid

            if total == N:
                return True
            elif total > N:
                hi = mid - 1
            else:
                lo = mid + 1

        return False