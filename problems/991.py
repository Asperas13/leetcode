class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        count = 0
        while Y > X:
            if Y & 1:
                Y += 1
            else:
                Y //= 2
            count += 1

        return count + X - Y