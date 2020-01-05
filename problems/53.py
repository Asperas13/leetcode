class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)

        max_cur = nums[0]
        max_global = nums[0]
        for i in range(1, len(nums)):
            max_cur = max(nums[i], max_cur + nums[i])
            if max_cur > max_global:
                max_global = max_cur

        return max_global