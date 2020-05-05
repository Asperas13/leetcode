class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            digits = 0
            while num > 0:
                num //= 10
                digits += 1

            count += 1 if digits & 1 == 0 else 0

        return count