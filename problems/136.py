class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        return total - 2 * (total - sum(set(nums)))


