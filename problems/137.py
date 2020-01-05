# [2, 2, 3, 2] -> 9
# [2, 3] -> 5
# 6


# [0, 1, 0, 1, 0, 1, 99] -> 102
# [0, 1, 99] -> 100

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        total_unique = sum(set(nums))

        return (total_unique * 3 - total) // 2