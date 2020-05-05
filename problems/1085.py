class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_elem = min(A)

        digit_sum = 0
        while min_elem > 0:
            digit_sum += min_elem % 10
            min_elem //= 10

        return 1 if digit_sum & 1 == 0 else 0