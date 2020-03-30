class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        if len(A) < 3:
            return 0

        i, j = 0, 1
        arithmetic_subsequences = 0
        while i < len(A) and j < len(A):
            diff = A[j] - A[j - 1]

            while j < len(A) and A[j] - A[j - 1] == diff:
                j += 1

            window_size = (j - i) - 2

            if window_size > 0:
                arithmetic_subsequences += ((1 + window_size) / 2) * window_size

            i = j - 1

        return int(arithmetic_subsequences)