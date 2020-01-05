class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        def _product(i, j, k):
            return nums[i] * nums[j] * nums[k]
        nums.sort()
        return max(_product(-1, -2, -3), _product(-1, 0, 1))