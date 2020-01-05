class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_profit = nums[0]
        for i in range(0, len(nums)):
            if i - 3 >= 0:
                nums[i] = max(nums[i - 2], nums[i - 3]) + nums[i]
            elif i - 2 >= 0:
                nums[i] = nums[i - 2] + nums[i]

            max_profit = max(max_profit, nums[i])

        return max_profit